"""Integration tests for complete MML to SMF conversion."""
import unittest
import sys
import os
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from pass1_parser import process_pass1
from pass2_ast import process_pass2
from pass3_events import process_pass3
from pass4_midi import process_pass4
from mido import MidiFile


class TestIntegration(unittest.TestCase):
    """Integration tests for full pipeline."""
    
    def test_full_pipeline_cde(self):
        """Test complete conversion of 'cde' to MIDI."""
        test_dir = '/tmp/test_integration'
        os.makedirs(test_dir, exist_ok=True)
        
        try:
            # Pass 1
            tokens = process_pass1('cde', f'{test_dir}/pass1.json')
            self.assertEqual(len(tokens), 3)
            
            # Pass 2
            ast = process_pass2(tokens, f'{test_dir}/pass2.json')
            self.assertEqual(len(ast['notes']), 3)
            self.assertEqual(ast['notes'][0]['pitch'], 60)  # C
            self.assertEqual(ast['notes'][1]['pitch'], 62)  # D
            self.assertEqual(ast['notes'][2]['pitch'], 64)  # E
            
            # Pass 3
            events = process_pass3(ast, f'{test_dir}/pass3.json')
            self.assertEqual(len(events), 6)  # 3 notes * 2 events each
            
            # Pass 4
            midi = process_pass4(events, f'{test_dir}/output.mid')
            self.assertTrue(os.path.exists(f'{test_dir}/output.mid'))
            
            # Verify MIDI file content
            loaded = MidiFile(f'{test_dir}/output.mid')
            note_messages = [msg for msg in loaded.tracks[0] 
                           if msg.type in ['note_on', 'note_off']]
            self.assertEqual(len(note_messages), 6)
            
            # Verify all debug JSONs exist
            self.assertTrue(os.path.exists(f'{test_dir}/pass1.json'))
            self.assertTrue(os.path.exists(f'{test_dir}/pass2.json'))
            self.assertTrue(os.path.exists(f'{test_dir}/pass3.json'))
            
        finally:
            # Cleanup
            for f in os.listdir(test_dir):
                os.remove(os.path.join(test_dir, f))
            os.rmdir(test_dir)
    
    def test_notes_60_62_64(self):
        """Test that 'cde' produces MIDI notes 60, 62, 64."""
        test_dir = '/tmp/test_notes'
        os.makedirs(test_dir, exist_ok=True)
        
        try:
            tokens = process_pass1('cde', f'{test_dir}/pass1.json')
            ast = process_pass2(tokens, f'{test_dir}/pass2.json')
            events = process_pass3(ast, f'{test_dir}/pass3.json')
            midi = process_pass4(events, f'{test_dir}/output.mid')
            
            # Load and verify notes
            loaded = MidiFile(f'{test_dir}/output.mid')
            note_ons = [msg for msg in loaded.tracks[0] 
                       if msg.type == 'note_on']
            
            notes = [msg.note for msg in note_ons]
            self.assertEqual(notes, [60, 62, 64])
            
        finally:
            # Cleanup
            for f in os.listdir(test_dir):
                os.remove(os.path.join(test_dir, f))
            os.rmdir(test_dir)


if __name__ == '__main__':
    unittest.main()
