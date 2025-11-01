#!/usr/bin/env python3
"""
MML to SMF Converter - Main Script

Converts Music Macro Language format string to Standard MIDI File
using a 4-pass architecture.
"""
import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from pass1_parser import process_pass1
from pass2_ast import process_pass2
from pass3_events import process_pass3
from pass4_midi import process_pass4


def main():
    """Main entry point for MML to SMF conversion."""
    parser = argparse.ArgumentParser(
        description='Convert Music Macro Language to Standard MIDI File'
    )
    parser.add_argument(
        'mml_string',
        type=str,
        help='MML format string (e.g., "cde")'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='output.mid',
        help='Output MIDI file path (default: output.mid)'
    )
    
    args = parser.parse_args()
    
    print(f"Converting MML: {args.mml_string}")
    
    # Pass 1: Parse MML string to tokens
    print("Pass 1: Parsing MML...")
    tokens = process_pass1(args.mml_string)
    print(f"  Generated {len(tokens)} tokens → pass1_tokens.json")
    
    # Pass 2: Convert tokens to AST
    print("Pass 2: Creating AST...")
    ast = process_pass2(tokens)
    print(f"  Generated AST with {len(ast.get('notes', []))} notes → pass2_ast.json")
    
    # Pass 3: Convert AST to MIDI events
    print("Pass 3: Creating MIDI events...")
    events = process_pass3(ast)
    print(f"  Generated {len(events)} events → pass3_events.json")
    
    # Pass 4: Convert events to SMF
    print("Pass 4: Creating MIDI file...")
    midi = process_pass4(events, args.output)
    print(f"  Generated MIDI file → {args.output}")
    
    print("\nConversion complete!")
    print(f"Output files:")
    print(f"  - pass1_tokens.json (debug)")
    print(f"  - pass2_ast.json (debug)")
    print(f"  - pass3_events.json (debug)")
    print(f"  - {args.output} (final output)")


if __name__ == '__main__':
    main()
