"""Tests for Pass 4: MIDI."""
import unittest
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from pass4_midi import events_to_midi, process_pass4
from mido import MidiFile


class TestPass4MIDI(unittest.TestCase):
    """Test cases for Pass 4 MIDI."""
    
    def test_events_to_midi_creates_file(self):
        """Test converting events to MIDI file."""
        events = [
            {'type': 'note_on', 'time': 0, 'note': 60, 'velocity': 64},
            {'type': 'note_off', 'time': 480, 'note': 60, 'velocity': 0}
        ]
        midi = events_to_midi(events)
        
        self.assertIsInstance(midi, MidiFile)
        self.assertEqual(len(midi.tracks), 1)
        self.assertGreater(len(midi.tracks[0]), 0)
    
    def test_midi_has_tempo(self):
        """Test that MIDI file has tempo message."""
        events = [
            {'type': 'note_on', 'time': 0, 'note': 60, 'velocity': 64},
            {'type': 'note_off', 'time': 480, 'note': 60, 'velocity': 0}
        ]
        midi = events_to_midi(events)
        
        # Check for tempo message
        has_tempo = any(msg.type == 'set_tempo' for msg in midi.tracks[0])
        self.assertTrue(has_tempo)
    
    def test_midi_has_end_of_track(self):
        """Test that MIDI file has end_of_track message."""
        events = [
            {'type': 'note_on', 'time': 0, 'note': 60, 'velocity': 64},
            {'type': 'note_off', 'time': 480, 'note': 60, 'velocity': 0}
        ]
        midi = events_to_midi(events)
        
        # Check for end_of_track message
        has_eot = any(msg.type == 'end_of_track' for msg in midi.tracks[0])
        self.assertTrue(has_eot)
    
    def test_process_pass4_saves_file(self):
        """Test that process_pass4 saves MIDI file."""
        output_file = '/tmp/test_output.mid'
        events = [
            {'type': 'note_on', 'time': 0, 'note': 60, 'velocity': 64},
            {'type': 'note_off', 'time': 480, 'note': 60, 'velocity': 0}
        ]
        
        try:
            result = process_pass4(events, output_file)
            self.assertTrue(os.path.exists(output_file))
            
            # Verify we can read it back
            loaded = MidiFile(output_file)
            self.assertEqual(len(loaded.tracks), 1)
        finally:
            if os.path.exists(output_file):
                os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
