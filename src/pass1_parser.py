"""
Pass 1: Parse MML string and create token list.
Outputs debug JSON.
"""
import json
from typing import List, Dict, Any


def parse_mml(mml_string: str) -> List[Dict[str, Any]]:
    """
    Parse MML string into tokens.
    
    Args:
        mml_string: MML format string (e.g., "cde")
        
    Returns:
        List of token dictionaries with type and value
    """
    tokens = []
    
    for char in mml_string.lower():
        if char in 'cdefgab':
            tokens.append({
                'type': 'note',
                'value': char
            })
    
    return tokens


def save_tokens_to_json(tokens: List[Dict[str, Any]], filepath: str) -> None:
    """
    Save tokens to JSON file for debugging.
    
    Args:
        tokens: List of token dictionaries
        filepath: Output JSON file path
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump({
            'pass': 1,
            'description': 'Parsed tokens',
            'tokens': tokens
        }, f, indent=2)


def process_pass1(mml_string: str, output_json: str = 'pass1_tokens.json') -> List[Dict[str, Any]]:
    """
    Execute Pass 1: Parse MML and save tokens.
    
    Args:
        mml_string: MML format string
        output_json: Output JSON file path
        
    Returns:
        List of tokens
    """
    tokens = parse_mml(mml_string)
    save_tokens_to_json(tokens, output_json)
    return tokens
