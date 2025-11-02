# Copilot Instructions for mmlabc-to-smf

## Project Architecture

This is a **4-pass compiler architecture** for converting Music Macro Language (MML) strings to Standard MIDI Files. Each pass is strictly sequential and outputs debug JSON files:

1. **Pass 1** (`src/pass1_parser.py`): MML string → tokens → `pass1_tokens.json`
2. **Pass 2** (`src/pass2_ast.py`): tokens → AST → `pass2_ast.json`
3. **Pass 3** (`src/pass3_events.py`): AST → MIDI events → `pass3_events.json`
4. **Pass 4** (`src/pass4_midi.py`): MIDI events → SMF file

**Key Design Constraint**: Each module is kept under ~100 lines for maintainability.

## Critical Development Patterns

### Module Structure
Every pass module follows this exact pattern:
```python
def convert_data(input_data):    # Core transformation logic
def save_to_json(data, filepath): # Debug output (passes 1-3 only)
def process_passN(input_data, output_path): # Entry point that calls both above
```

### Path Management
- Main script adds `src/` to path: `sys.path.insert(0, str(Path(__file__).parent / 'src'))`
- Tests add src to path: `sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))`
- All imports are direct: `from pass1_parser import process_pass1`

### Testing Strategy
- **Unit tests**: Test each pass's core transformation function (`test_pass1.py` - `test_pass4.py`)
- **Integration tests**: Test complete pipeline in `test_integration.py`
- **File cleanup**: Tests create temp files in `/tmp/test_*` and clean up in `finally` blocks
- **Assertion pattern**: Verify both data structure and file existence

## Data Flow Contracts

### Pass 1 Output (tokens)
```python
[{'type': 'note', 'value': 'c'}, {'type': 'note', 'value': 'd'}]
```

### Pass 2 Output (AST)
```python
{'type': 'sequence', 'notes': [{'type': 'note', 'pitch': 60, 'name': 'c'}]}
```

### Pass 3 Output (events)
```python
[{'type': 'note_on', 'time': 0, 'note': 60, 'velocity': 64}]
```

### MIDI Note Mapping
Use `NOTE_TO_MIDI` dict in `pass2_ast.py`: `c=60, d=62, e=64, f=65, g=67, a=69, b=71`

## Development Workflow

### Running Tests
```bash
python -m unittest discover -s tests -p "test_*.py" -v  # All tests
python -m unittest tests.test_integration                # Integration only
```

### Running Main CLI
```bash
python mml_to_smf.py "cde"                              # Basic usage
python mml_to_smf.py "cde" -o output.mid               # Custom output
```

### Code Quality
- **Linting**: Uses Ruff with 120 char line length, double quotes, space indents
- **Dependencies**: Only `mido==1.3.2` for MIDI file handling
- **Python**: Requires 3.8+ (see `setup.py`)

## Key Implementation Details

### Time/Duration Logic (Pass 3)
- Default duration: 480 ticks (quarter note)
- Sequential timing: `time += duration` after each note
- Each note generates 2 events: note_on at `time`, note_off at `time + duration`

### MIDI File Structure (Pass 4)
- Always includes tempo message: `MetaMessage('set_tempo', tempo=500000, time=0)` (120 BPM)
- Events sorted by time before conversion to delta times
- Always ends with `MetaMessage('end_of_track', time=0)`

### Debug Output Convention
Every debug JSON follows this structure:
```python
{'pass': N, 'description': 'Pass description', 'data_key': actual_data}
```

When modifying passes, maintain the strict input/output contracts and ~100 line limit per file.
