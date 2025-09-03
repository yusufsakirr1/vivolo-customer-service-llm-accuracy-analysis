#!/usr/bin/env python3
import pandas as pd
import numpy as np

def analyze_llm_accuracy(csv_file_path):
    """
    Analyze the accuracy of LLM predictions compared to manual labels.
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path, sep=';')
    
    # Clean column names by removing BOM and extra spaces
    df.columns = df.columns.str.replace('\ufeff', '').str.strip()
    
    # Print basic info about the dataset
    print("="*80)
    print("LLM ACCURACY ANALYSIS REPORT")
    print("="*80)
    print(f"\nDataset Overview:")
    print(f"Total conversations analyzed: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    
    # Print first few rows to understand data structure
    print(f"\nFirst 3 rows:")
    print(df.head(3).to_string())
    
    # Define the comparison columns
    comparisons = {
        'Topic Classification': ('LLM Topic', 'Manuel Topic'),
        'Sentiment Analysis': ('LLM Sentiment', 'Manuel Sentiment'), 
        'Bot Answered': ('LLM Bot Answered', 'Manuel Bot Answered')
    }
    
    results = {}
    detailed_comparisons = {}
    
    print(f"\n" + "="*80)
    print("DETAILED ACCURACY ANALYSIS")
    print("="*80)
    
    for category, (llm_col, manual_col) in comparisons.items():
        print(f"\n{category.upper()} ANALYSIS:")
        print("-" * 50)
        
        # Clean the data - remove extra spaces and handle NaN
        llm_vals = df[llm_col].fillna('').astype(str).str.strip()
        manual_vals = df[manual_col].fillna('').astype(str).str.strip()
        
        # Calculate accuracy
        matches = (llm_vals == manual_vals)
        accuracy = matches.sum() / len(matches)
        total_comparisons = len(matches)
        correct_predictions = matches.sum()
        incorrect_predictions = total_comparisons - correct_predictions
        
        results[category] = {
            'accuracy': accuracy,
            'correct': correct_predictions,
            'incorrect': incorrect_predictions,
            'total': total_comparisons
        }
        
        print(f"Total comparisons: {total_comparisons}")
        print(f"Correct predictions: {correct_predictions}")
        print(f"Incorrect predictions: {incorrect_predictions}")
        print(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
        
        # Show unique values in each column
        print(f"\nUnique LLM {category} values: {sorted(llm_vals.unique())}")
        print(f"Unique Manual {category} values: {sorted(manual_vals.unique())}")
        
        # Show mismatches
        mismatches = df[~matches][['Konuşma No', 'Konuşma ID', llm_col, manual_col]]
        if len(mismatches) > 0:
            print(f"\nMismatches ({len(mismatches)} total):")
            print(mismatches.to_string(index=False))
        
        # Store detailed comparison data
        comparison_df = df[['Konuşma No', 'Konuşma ID', llm_col, manual_col]].copy()
        comparison_df['Match'] = matches
        detailed_comparisons[category] = comparison_df
    
    # Calculate overall accuracy
    total_predictions = sum([results[cat]['total'] for cat in results])
    total_correct = sum([results[cat]['correct'] for cat in results])
    overall_accuracy = total_correct / total_predictions if total_predictions > 0 else 0
    
    print(f"\n" + "="*80)
    print("OVERALL SUMMARY")
    print("="*80)
    print(f"Total predictions across all categories: {total_predictions}")
    print(f"Total correct predictions: {total_correct}")
    print(f"Overall accuracy: {overall_accuracy:.4f} ({overall_accuracy*100:.2f}%)")
    
    print(f"\nAccuracy by category:")
    for category, result in results.items():
        print(f"  {category}: {result['accuracy']:.4f} ({result['accuracy']*100:.2f}%)")
    
    return results, detailed_comparisons, df

if __name__ == "__main__":
    csv_file = "/Users/yusufi/Desktop/Grispi Ödev/llm_analysis_v7_final_results.csv"
    results, detailed_comparisons, raw_data = analyze_llm_accuracy(csv_file)
    
    # Save detailed comparison data to separate CSV files
    for category, comparison_df in detailed_comparisons.items():
        filename = f"/Users/yusufi/Desktop/Grispi Ödev/detailed_{category.lower().replace(' ', '_')}_comparison.csv"
        comparison_df.to_csv(filename, index=False)
        print(f"\nDetailed {category} comparison saved to: {filename}")