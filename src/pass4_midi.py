"""
Pass 4: Convert MIDI events to Standard MIDI File.
Outputs SMF file.
"""
from typing import List, Dict, Any
from mido import MidiFile, MidiTrack, Message, MetaMessage


def events_to_midi(events: List[Dict[str, Any]]) -> MidiFile:
    """
    Convert MIDI events to MidiFile object.
    
    Args:
        events: List of MIDI event dictionaries from Pass 3
        
    Returns:
        MidiFile object
    """
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    
    # Add tempo (500000 microseconds per beat = 120 BPM)
    track.append(MetaMessage('set_tempo', tempo=500000, time=0))
    
    # Sort events by time
    sorted_events = sorted(events, key=lambda e: e['time'])
    
    prev_time = 0
    for event in sorted_events:
        delta_time = event['time'] - prev_time
        
        if event['type'] == 'note_on':
            track.append(Message('note_on',
                               note=event['note'],
                               velocity=event['velocity'],
                               time=delta_time))
        elif event['type'] == 'note_off':
            track.append(Message('note_off',
                               note=event['note'],
                               velocity=event['velocity'],
                               time=delta_time))
        
        prev_time = event['time']
    
    # End of track
    track.append(MetaMessage('end_of_track', time=0))
    
    return mid


def save_midi_file(midi: MidiFile, filepath: str) -> None:
    """
    Save MidiFile to SMF file.
    
    Args:
        midi: MidiFile object
        filepath: Output SMF file path
    """
    midi.save(filepath)


def process_pass4(events: List[Dict[str, Any]], output_smf: str = 'output.mid') -> MidiFile:
    """
    Execute Pass 4: Create SMF from MIDI events.
    
    Args:
        events: List of MIDI events from Pass 3
        output_smf: Output SMF file path
        
    Returns:
        MidiFile object
    """
    midi = events_to_midi(events)
    save_midi_file(midi, output_smf)
    return midi
