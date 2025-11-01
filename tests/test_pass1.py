"""Tests for Pass 1: Parser."""
import unittest
import sys
import os
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from pass1_parser import parse_mml, process_pass1


class TestPass1Parser(unittest.TestCase):
    """Test cases for Pass 1 parser."""
    
    def test_parse_simple_notes(self):
        """Test parsing simple note sequence."""
        result = parse_mml('cde')
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], {'type': 'note', 'value': 'c'})
        self.assertEqual(result[1], {'type': 'note', 'value': 'd'})
        self.assertEqual(result[2], {'type': 'note', 'value': 'e'})
    
    def test_parse_uppercase(self):
        """Test parsing uppercase notes."""
        result = parse_mml('CDE')
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], {'type': 'note', 'value': 'c'})
    
    def test_parse_all_notes(self):
        """Test parsing all note names."""
        result = parse_mml('cdefgab')
        self.assertEqual(len(result), 7)
        expected_notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
        for i, note in enumerate(expected_notes):
            self.assertEqual(result[i]['value'], note)
    
    def test_parse_empty_string(self):
        """Test parsing empty string."""
        result = parse_mml('')
        self.assertEqual(len(result), 0)
    
    def test_process_pass1_creates_json(self):
        """Test that process_pass1 creates JSON file."""
        output_file = '/tmp/test_pass1.json'
        try:
            result = process_pass1('cde', output_file)
            self.assertTrue(os.path.exists(output_file))
            
            with open(output_file, 'r') as f:
                data = json.load(f)
            
            self.assertEqual(data['pass'], 1)
            self.assertEqual(len(data['tokens']), 3)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
