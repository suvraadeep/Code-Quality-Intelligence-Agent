# Code Quality Intelligence Report
Generated on: 2025-09-11 19:52:38

## Summary
- **Files Analyzed**: 2
- **Total Issues**: 11

### Metrics
- **Complexity Score**: 2.2
- **Maintainability Score**: 0.0
- **Security Score**: 0.0
- **Overall Score**: 0.0

## Issues
### High Issues (3)
#### pattern
**Description**: Use of eval() is dangerous
**Location**: `sample_code\module_a.py:14`

#### pattern
**Description**: Use of eval() is dangerous
**Location**: `sample_code\module_a.py:15`

#### pattern
**Description**: Unsafe deserialization (pickle)
**Location**: `sample_code\module_b.py:16`

### Low Issues (8)
#### missing_docstring
**Description**: Function "add" missing docstring
**Location**: `sample_code\module_a.py:5`

#### missing_docstring
**Description**: Function "dangerous_eval" missing docstring
**Location**: `sample_code\module_a.py:14`

#### pattern
**Description**: Bare except detected; catch specific exceptions
**Location**: `sample_code\module_a.py:20`

#### missing_docstring
**Description**: Function "compute" missing docstring
**Location**: `sample_code\module_b.py:4`

#### missing_docstring
**Description**: Function "load_pickle" missing docstring
**Location**: `sample_code\module_b.py:14`
