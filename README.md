# mmlabc-to-smf

A conversion tool from Music Macro Language (MML) to Standard MIDI File (SMF)

<p align="left">
  <a href="README.ja.md"><img src="https://img.shields.io/badge/🇯🇵-Japanese-red.svg" alt="Japanese"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/🇺🇸-English-blue.svg" alt="English"></a>
</p>

## 状況

アーカイブします。後継のRust版を開発します。

このリポジトリの用途は、Pythonによる最低限の参考用のコードを提供する用です。

## Overview

This project converts Music Macro Language strings into Standard MIDI Files using a 4-pass architecture with comprehensive debug output.

## Features

- **4-Pass Architecture**:
  - Pass 1: Parses MML strings into tokens (outputs `pass1_tokens.json`)
  - Pass 2: Transforms tokens into an Abstract Syntax Tree (AST) (outputs `pass2_ast.json`)
  - Pass 3: Generates MIDI events from the AST (outputs `pass3_events.json`)
  - Pass 4: Creates the Standard MIDI File (outputs a `.mid` file)
- **Debug JSON Output**: Each pass saves its intermediate results as JSON for debugging
- **Test-Driven Development**: Comprehensive test suite including unit and integration tests
- **Modular Design**: Each pass is implemented in approximately 100 lines of code or less per file

## Requirements

- Python 3.8 or higher
- mido (Python MIDI library)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python mml_to_smf.py "cde"
```

This converts the MML string "cde" (notes C, D, E) as follows:
- MIDI notes 60, 62, 64 (Middle C, D, E)
- Output file: `output.mid`
- Debug files: `pass1_tokens.json`, `pass2_ast.json`, `pass3_events.json`

### Custom Output File

```bash
python mml_to_smf.py "cde" -o my_song.mid
```

### Supported Notes

Currently supports basic note names: `c`, `d`, `e`, `f`, `g`, `a`, `b`

## Example Run

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
│   ├── pass1_parser.py    # Pass 1: MML Parsing
│   ├── pass2_ast.py        # Pass 2: AST Creation
│   ├── pass3_events.py     # Pass 3: Event Generation
│   └── pass4_midi.py       # Pass 4: MIDI File Creation
├── tests/
│   ├── test_pass1.py       # Pass 1 Unit Tests
│   ├── test_pass2.py       # Pass 2 Unit Tests
│   ├── test_pass3.py       # Pass 3 Unit Tests
│   ├── test_pass4.py       # Pass 4 Unit Tests
│   └── test_integration.py # Integration Tests
├── mml_to_smf.py          # Main CLI Script
├── requirements.txt        # Python Dependencies
└── README.md              # This file
```

## Testing

To run all tests:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

To run specific test files:

```bash
python -m unittest tests.test_integration
```

## Development

This project adheres to Test-Driven Development (TDD) principles:

1.  Each module is kept to approximately 100 lines of code or less.
2.  Each pass has corresponding unit tests.
3.  Integration tests validate the complete pipeline.
4.  Debug JSON outputs are available at each stage for troubleshooting.

## License

See the LICENSE file for more details.

※ The English version of README.md is automatically generated from README.ja.md using Gemini's translation via GitHub Actions.
