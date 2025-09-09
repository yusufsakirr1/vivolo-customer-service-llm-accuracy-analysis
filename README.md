# 🤖 Hera AI Customer Service LLM Accuracy Analysis

> A comprehensive analysis tool for evaluating Large Language Model performance in customer service conversation classification tasks.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.0+-green.svg)](https://pandas.pydata.org/)
[![Student Project](https://img.shields.io/badge/Project-Student-orange.svg)]()
[![Analysis Status](https://img.shields.io/badge/Analysis-Complete-success.svg)]()

## 🎯 Project Overview

This project evaluates the accuracy of **Hera AI**, a customer service chatbot, by comparing LLM-generated classifications with manual human annotations across three key dimensions:

- **🏷️ Topic Classification** - Categorizing conversation topics (weddings, events, etc.)
- **💭 Sentiment Analysis** - Determining customer emotional state
- **✅ Bot Response Quality** - Assessing whether the bot successfully helped the customer

## 📊 Key Results

### 🎉 Overall Performance
- **Total Accuracy: 84.67%** (127/150 predictions correct)
- **Conversations Analyzed: 50**
- **Classification Categories: 3**

### 📈 Category Breakdown

| Category | Accuracy | Performance | Status |
|----------|----------|-------------|---------|
| **Sentiment Analysis** | 98.00% (49/50) | Excellent ⭐⭐⭐⭐⭐ | Production Ready |
| **Topic Classification** | 88.00% (44/50) | Good ⭐⭐⭐⭐ | Minor Tuning Needed |
| **Bot Response Quality** | 68.00% (34/50) | Needs Improvement ⭐⭐⭐ | Requires Enhancement |

## 🚀 Features

- **Automated LLM Evaluation** - Compare AI predictions with human annotations
- **Multi-dimensional Analysis** - Topic, sentiment, and response quality metrics
- **Detailed Error Analysis** - Identify specific failure patterns
- **Professional Reporting** - Generate comprehensive analysis reports
- **Export Capabilities** - Output results in multiple formats (CSV, TXT)

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pandas library
- numpy library

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yusufsakir1/hera-ai-customer-service-llm-accuracy-analysis.git
   cd hera-ai-customer-service-llm-accuracy-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy
   ```

3. **Run the analysis**
   ```bash
   python analyze_llm_accuracy.py
   ```

## 📁 Project Structure

```
├── analyze_llm_accuracy.py              # Main analysis script
├── llm_analysis_v7_final.py            # Advanced analysis tools
├── llm_analysis_prompt.txt              # LLM prompt engineering file
├── llm_analysis_v7_final_results.csv   # Main dataset
├── detailed_*_comparison.csv            # Detailed comparison files
├── llm_accuracy_analysis_summary.txt   # Comprehensive report
└── last-500-conversation-dugunbuketi.json # Raw conversation data
```

## 💡 Usage

### Basic Analysis
```python
from analyze_llm_accuracy import analyze_llm_accuracy

# Run complete accuracy analysis
results = analyze_llm_accuracy('llm_analysis_v7_final_results.csv')
```

### Custom Analysis
```python
import pandas as pd

# Load your own dataset
df = pd.read_csv('your_data.csv', sep=';')

# Define comparison columns
comparisons = {
    'Topic Classification': ('LLM Topic', 'Manual Topic'),
    'Sentiment Analysis': ('LLM Sentiment', 'Manual Sentiment'),
    'Bot Answered': ('LLM Bot Answered', 'Manual Bot Answered')
}

# Run analysis (see analyze_llm_accuracy.py for full implementation)
```

## 📊 Analysis Results

### 🎯 Accuracy Metrics

| Metric | Sentiment | Topic | Bot Response | Overall |
|--------|-----------|-------|--------------|---------|
| **Accuracy** | 98.00% | 88.00% | 68.00% | 84.67% |
| **Correct** | 49/50 | 44/50 | 34/50 | 127/150 |
| **Errors** | 1 | 6 | 16 | 23 |
| **Grade** | A+ | B+ | C | B |

### 🔍 Error Analysis

**Bot Response Issues (16 errors):**
- False Negatives: 15 cases (LLM says "No", Manual says "Yes")
- False Positives: 1 case (LLM says "Yes", Manual says "No")
- **Root Cause:** Conservative prediction tendency

**Topic Classification Issues (6 errors):**
- Confusion between similar event types (wedding/circumcision)
- Ambiguity in engagement-related subcategories

## 🔬 Technical Details

- **Data Source:** Apple Numbers spreadsheet (.numbers)
- **Analysis Method:** Comparative analysis using Python pandas
- **Metrics:** Simple accuracy ratio
- **Dataset Size:** 50 conversations × 3 categories = 150 predictions
- **LLM Model:** Hera AI (proprietary customer service model)

## 📈 Business Impact

This analysis reveals that:
1. **Sentiment analysis is production-ready** with 98% accuracy
2. **Topic classification performs well** but needs refinement for edge cases
3. **Bot response evaluation requires significant improvement** - currently too conservative

## 🎓 About This Project

This is a **student project** developed to demonstrate LLM evaluation techniques and data analysis skills. The project showcases:
- Data science methodologies
- Machine learning model evaluation
- Statistical analysis and reporting
- Professional documentation practices

## 📞 Contact

- **Author:** Yusuf Şakir (Student)
- **Project:** Hera AI Customer Service Analysis
- **Repository:** [GitHub](https://github.com/yusufsakir1/hera-ai-customer-service-llm-accuracy-analysis)

---

⭐ **Star this repository** if you found it helpful!