# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a multi-language samples repository containing code examples and tutorials across various programming languages and technologies. The repository is organized by language/technology, each in its own directory with standalone examples and small projects.

## Directory Structure

### Core Language Directories
- **`python/`** - Python examples including algorithms, data structures, game development (pygame), numerical computing (numpy), and various coding challenges
- **`node_js/`** - Node.js server examples, data structures, and utilities  
- **`javascript/`** - Browser-based JavaScript including Canvas/WebGL graphics, UI components, and frontend examples
- **`golang/`** - Go examples covering algorithms, numerical methods, and SDL2 graphics programming
- **`rust/`** - Rust projects including CLI tools, Advent of Code solutions, and mathematical computations (Mandelbrot, Lychrel numbers)
- **`java/`** - Java algorithm implementations
- **`ruby_prog/`** - Ruby examples including graph algorithms and Qt bindings
- **`cprog/`** - C/C++ system programming examples
- **`scala_ex/`** - Scala functional programming examples

### Special Directories
- **`ai_examples/`** - Machine learning examples using transformers, torch, scikit-learn
- **`docker/`** - Containerized applications and services
- **`minecraft/`** - Minecraft server deployment tools

## Common Development Commands

### Python Development
```bash
# Set up Python virtual environment (if not exists)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS

# Install AI/ML dependencies
pip install -r ai_examples/requirements.txt

# Install specific project dependencies
pip install -r python/pygame/requirements.txt
pip install -r python/numpy/requirements.txt
pip install -r python/boids/requirements.txt

# Run Python examples
python python/roman.py
python python/algorithms/sum_test.py
```

### Node.js Development
```bash
# Install dependencies for WebGL project
cd javascript/webgl && npm install

# Install dependencies for specific Node.js projects
cd node_js/drone && npm install
cd node_js/scroll && npm install

# Start Express applications
npm start
```

### Go Development
```bash
# Run Go programs directly
go run golang/fibonacci.go
go run golang/newton.go

# For projects with SDL2 dependencies
cd golang/sdl2
go mod tidy && go run .
```

### Rust Development
```bash
# Build and run Rust projects
cd rust/guessing_game && cargo run
cd rust/mandelbrot && cargo run --release
cd rust/lychrel && cargo build --release

# For performance-critical applications, always use --release
cargo run --release
```

### Docker Development
```bash
# Build and run containerized applications
docker-compose up

# Build Minecraft server
cd minecraft && make build
```

## Testing Approach

- Python tests are typically standalone scripts with `if __name__ == "__main__"` blocks
- Test files follow the pattern `*test*.py`, `*test*.js`, etc.
- Most examples are self-contained with test cases included in the main files
- Run tests by executing the individual test files directly

## Development Environment

- **Editor Config**: The repository uses `.editorconfig` for C++ formatting standards
- **Virtual Environments**: Python projects use `.venv` directories (gitignored)
- **Package Management**: Each language uses its standard package manager (pip, npm, cargo, go mod)

## Code Architecture Notes

### Python Structure
- Examples range from simple algorithmic solutions to complex ML workflows
- pygame directory contains game development examples
- numpy directory has scientific computing examples
- Most files are self-contained examples rather than libraries

### JavaScript/Node.js Structure  
- Browser-based examples in `javascript/` focus on graphics and UI
- Server-side examples in `node_js/` include HTTP servers, data processing, and APIs
- WebGL project follows Express.js application structure

### Systems Programming
- Go examples demonstrate concurrency patterns and numerical computation
- Rust projects showcase memory safety and performance optimization
- C programs focus on system-level programming concepts

## Language-Specific Notes

- **Python**: Uses both procedural and object-oriented approaches; includes ML/AI examples
- **JavaScript**: Emphasizes DOM manipulation, Canvas graphics, and async programming  
- **Go**: Focuses on simplicity, concurrency, and performance
- **Rust**: Emphasizes memory safety, zero-cost abstractions, and systems programming
- **Java**: Classic OOP examples and algorithm implementations

## Build Systems

- Most examples are single-file programs that run directly
- Complex projects use standard build tools (Cargo for Rust, npm for Node.js, go mod for Go)
- Makefiles are used for C/C++ compilation and Docker image building