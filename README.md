# mmlabc-to-smf

Music Macro Language (MML) to Standard MIDI File (SMF) Converter

## Overview

This project converts Music Macro Language format strings into Standard MIDI Files using a 4-pass architecture with comprehensive debug output.

## Features

- **4-Pass Architecture**: 
  - Pass 1: Parse MML string into tokens (outputs `pass1_tokens.json`)
  - Pass 2: Convert tokens to Abstract Syntax Tree (outputs `pass2_ast.json`)
  - Pass 3: Generate MIDI events from AST (outputs `pass3_events.json`)
  - Pass 4: Create Standard MIDI File (outputs `.mid` file)
- **Debug JSON Output**: Each pass saves intermediate results as JSON for debugging
- **Test-Driven Development**: Comprehensive test suite with unit and integration tests
- **Modular Design**: Each pass is implemented in ~100 lines or less per file

## Requirements

- Python 3.8 or higher
- mido (Python MIDI library)
- tree-sitter (Parser library)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python mml_to_smf.py "cde"
```

This converts the MML string "cde" (notes C, D, E) into:
- MIDI notes 60, 62, 64 (Middle C, D, E)
- Output file: `output.mid`
- Debug files: `pass1_tokens.json`, `pass2_ast.json`, `pass3_events.json`

### Custom Output File

```bash
python mml_to_smf.py "cde" -o my_song.mid
```

### Supported Notes

Currently supports basic note names: `c`, `d`, `e`, `f`, `g`, `a`, `b`

## Example

```bash
$ python mml_to_smf.py "cde"
Converting MML: cde
Pass 1: Parsing MML...
  Generated 3 tokens → pass1_tokens.json
Pass 2: Creating AST...
  Generated AST with 3 notes → pass2_ast.json
Pass 3: Creating MIDI events...
  Generated 6 events → pass3_events.json
Pass 4: Creating MIDI file...
  Generated MIDI file → output.mid

Conversion complete!
Output files:
  - pass1_tokens.json (debug)
  - pass2_ast.json (debug)
  - pass3_events.json (debug)
  - output.mid (final output)
```

## Project Structure

```
mmlabc-to-smf/
├── src/
│   ├── pass1_parser.py    # Pass 1: MML parsing
│   ├── pass2_ast.py        # Pass 2: AST creation
│   ├── pass3_events.py     # Pass 3: Event generation
│   └── pass4_midi.py       # Pass 4: MIDI file creation
├── tests/
│   ├── test_pass1.py       # Unit tests for Pass 1
│   ├── test_pass2.py       # Unit tests for Pass 2
│   ├── test_pass3.py       # Unit tests for Pass 3
│   ├── test_pass4.py       # Unit tests for Pass 4
│   └── test_integration.py # Integration tests
├── mml_to_smf.py          # Main CLI script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Testing

Run all tests:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Run specific test file:

```bash
python -m unittest tests.test_integration
```

## Development

This project follows Test-Driven Development (TDD) principles:

1. Each module is kept under ~100 lines
2. Each pass has corresponding unit tests
3. Integration tests verify the complete pipeline
4. Debug JSON output at each stage for troubleshooting

## License

See LICENSE file for details.