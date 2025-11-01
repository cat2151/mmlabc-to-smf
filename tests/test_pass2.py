"""Tests for Pass 2: AST."""
import unittest
import sys
import os
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from pass2_ast import tokens_to_ast, process_pass2, NOTE_TO_MIDI


class TestPass2AST(unittest.TestCase):
    """Test cases for Pass 2 AST."""
    
    def test_tokens_to_ast_simple(self):
        """Test converting tokens to AST."""
        tokens = [
            {'type': 'note', 'value': 'c'},
            {'type': 'note', 'value': 'd'},
            {'type': 'note', 'value': 'e'}
        ]
        ast = tokens_to_ast(tokens)
        
        self.assertEqual(ast['type'], 'sequence')
        self.assertEqual(len(ast['notes']), 3)
        self.assertEqual(ast['notes'][0]['pitch'], 60)  # C
        self.assertEqual(ast['notes'][1]['pitch'], 62)  # D
        self.assertEqual(ast['notes'][2]['pitch'], 64)  # E
    
    def test_note_to_midi_mapping(self):
        """Test MIDI note number mapping."""
        self.assertEqual(NOTE_TO_MIDI['c'], 60)
        self.assertEqual(NOTE_TO_MIDI['d'], 62)
        self.assertEqual(NOTE_TO_MIDI['e'], 64)
    
    def test_ast_includes_note_names(self):
        """Test that AST includes note names."""
        tokens = [{'type': 'note', 'value': 'c'}]
        ast = tokens_to_ast(tokens)
        self.assertEqual(ast['notes'][0]['name'], 'c')
    
    def test_process_pass2_creates_json(self):
        """Test that process_pass2 creates JSON file."""
        output_file = '/tmp/test_pass2.json'
        tokens = [{'type': 'note', 'value': 'c'}]
        
        try:
            result = process_pass2(tokens, output_file)
            self.assertTrue(os.path.exists(output_file))
            
            with open(output_file, 'r') as f:
                data = json.load(f)
            
            self.assertEqual(data['pass'], 2)
            self.assertIn('ast', data)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
