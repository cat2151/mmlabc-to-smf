"""
Pass 2: Convert tokens to AST (Abstract Syntax Tree).
Outputs debug JSON.
"""
import json
from typing import List, Dict, Any


NOTE_TO_MIDI = {
    'c': 60,  # Middle C (C4)
    'd': 62,
    'e': 64,
    'f': 65,
    'g': 67,
    'a': 69,
    'b': 71
}


def tokens_to_ast(tokens: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Convert tokens to AST structure.
    
    Args:
        tokens: List of token dictionaries
        
    Returns:
        AST dictionary with note events
    """
    ast = {
        'type': 'sequence',
        'notes': []
    }
    
    for token in tokens:
        if token['type'] == 'note':
            note_char = token['value']
            midi_note = NOTE_TO_MIDI.get(note_char, 60)
            ast['notes'].append({
                'type': 'note',
                'pitch': midi_note,
                'name': note_char
            })
    
    return ast


def save_ast_to_json(ast: Dict[str, Any], filepath: str) -> None:
    """
    Save AST to JSON file for debugging.
    
    Args:
        ast: AST dictionary
        filepath: Output JSON file path
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump({
            'pass': 2,
            'description': 'Abstract Syntax Tree',
            'ast': ast
        }, f, indent=2)


def process_pass2(tokens: List[Dict[str, Any]], output_json: str = 'pass2_ast.json') -> Dict[str, Any]:
    """
    Execute Pass 2: Create AST from tokens.
    
    Args:
        tokens: List of tokens from Pass 1
        output_json: Output JSON file path
        
    Returns:
        AST dictionary
    """
    ast = tokens_to_ast(tokens)
    save_ast_to_json(ast, output_json)
    return ast
