# Wind Energy Analysis Project

This project analyzes wind energy data across multiple countries, providing insights through data profiling, cleaning, and visualization.

## Project Structure

```
.
├── data/                   # Raw and processed data files
├── notebooks/             # Jupyter notebooks for EDA
├── src/                   # Source code
│   ├── data/             # Data processing modules
│   ├── visualization/    # Visualization modules
│   └── utils/            # Utility functions
├── app/                   # Streamlit dashboard
├── tests/                # Unit tests
└── .github/workflows/    # CI/CD configuration
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Components

### Data Analysis
- EDA notebooks for each country
- Data cleaning and preprocessing
- Statistical analysis and visualization

### Interactive Dashboard
- Streamlit-based dashboard
- Interactive visualizations
- Country comparison features

## Development Workflow

1. Create a new branch for each feature
2. Follow PEP 8 style guide
3. Write clear commit messages
4. Run tests before committing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License 