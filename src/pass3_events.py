"""
Pass 3: Convert AST to MIDI events.
Outputs debug JSON.
"""
import json
from typing import List, Dict, Any


def ast_to_events(ast: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Convert AST to MIDI event list.
    
    Args:
        ast: AST dictionary from Pass 2
        
    Returns:
        List of MIDI event dictionaries
    """
    events = []
    time = 0
    duration = 480  # Default duration in ticks (quarter note at 480 ticks per beat)
    
    for note in ast.get('notes', []):
        # Note on event
        events.append({
            'type': 'note_on',
            'time': time,
            'note': note['pitch'],
            'velocity': 64
        })
        
        # Note off event
        events.append({
            'type': 'note_off',
            'time': time + duration,
            'note': note['pitch'],
            'velocity': 0
        })
        
        time += duration
    
    return events


def save_events_to_json(events: List[Dict[str, Any]], filepath: str) -> None:
    """
    Save events to JSON file for debugging.
    
    Args:
        events: List of MIDI event dictionaries
        filepath: Output JSON file path
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump({
            'pass': 3,
            'description': 'MIDI events',
            'events': events
        }, f, indent=2)


def process_pass3(ast: Dict[str, Any], output_json: str = 'pass3_events.json') -> List[Dict[str, Any]]:
    """
    Execute Pass 3: Create MIDI events from AST.
    
    Args:
        ast: AST dictionary from Pass 2
        output_json: Output JSON file path
        
    Returns:
        List of MIDI events
    """
    events = ast_to_events(ast)
    save_events_to_json(events, output_json)
    return events
