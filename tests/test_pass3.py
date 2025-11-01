"""Tests for Pass 3: Events."""
import unittest
import sys
import os
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from pass3_events import ast_to_events, process_pass3


class TestPass3Events(unittest.TestCase):
    """Test cases for Pass 3 events."""
    
    def test_ast_to_events_simple(self):
        """Test converting AST to MIDI events."""
        ast = {
            'type': 'sequence',
            'notes': [
                {'type': 'note', 'pitch': 60, 'name': 'c'},
                {'type': 'note', 'pitch': 62, 'name': 'd'},
                {'type': 'note', 'pitch': 64, 'name': 'e'}
            ]
        }
        events = ast_to_events(ast)
        
        # Should have note_on and note_off for each note
        self.assertEqual(len(events), 6)
        
        # First note on
        self.assertEqual(events[0]['type'], 'note_on')
        self.assertEqual(events[0]['note'], 60)
        self.assertEqual(events[0]['time'], 0)
        
        # First note off
        self.assertEqual(events[1]['type'], 'note_off')
        self.assertEqual(events[1]['note'], 60)
        self.assertEqual(events[1]['time'], 480)
    
    def test_events_sequential_timing(self):
        """Test that events have correct sequential timing."""
        ast = {
            'type': 'sequence',
            'notes': [
                {'type': 'note', 'pitch': 60, 'name': 'c'},
                {'type': 'note', 'pitch': 62, 'name': 'd'}
            ]
        }
        events = ast_to_events(ast)
        
        # Second note should start after first note ends
        note_on_times = [e['time'] for e in events if e['type'] == 'note_on']
        self.assertEqual(note_on_times[0], 0)
        self.assertEqual(note_on_times[1], 480)
    
    def test_process_pass3_creates_json(self):
        """Test that process_pass3 creates JSON file."""
        output_file = '/tmp/test_pass3.json'
        ast = {
            'type': 'sequence',
            'notes': [{'type': 'note', 'pitch': 60, 'name': 'c'}]
        }
        
        try:
            result = process_pass3(ast, output_file)
            self.assertTrue(os.path.exists(output_file))
            
            with open(output_file, 'r') as f:
                data = json.load(f)
            
            self.assertEqual(data['pass'], 3)
            self.assertIn('events', data)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
