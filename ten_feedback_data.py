import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# --- 1. CONFIGURATION ---

# Geography Mapping for Power BI Map
GEO_MAP = {
    'Paris':        {'Country': 'France', 'Lat': 48.8566, 'Long': 2.3522},
    'Houston':      {'Country': 'USA',    'Lat': 29.7604, 'Long': -95.3698},
    'Rome':         {'Country': 'Italy',  'Lat': 41.9028, 'Long': 12.4964},
    'Abu Dhabi':    {'Country': 'UAE',    'Lat': 24.4539, 'Long': 54.3773},
    'Kuala Lumpur': {'Country': 'Malaysia','Lat': 3.1390,  'Long': 101.6869}
}

# Category Keywords
CATEGORIES = {
    'HSE': ['safety', 'injury', 'accident', 'fire', 'hazard', 'ppe', 'spill', 'risk', 'compliance', 'environment', 'health', 'warning', 'alarm'],
    'IT': ['software', 'laptop', 'server', 'internet', 'wifi', 'login', 'password', 'screen', 'network', 'vpn', 'printer', 'computer', 'mouse', 'install', 'update'],
    'Procurement': ['supplier', 'vendor', 'delivery', 'shipment', 'invoice', 'cost', 'price', 'purchase', 'contract', 'lead time'],
    'Engineering': ['design', 'drawing', 'cad', 'simulation', 'calculation', 'technical', 'specifications', 'piping', 'structural', 'p&id'],
    'HR': ['salary', 'promotion', 'manager', 'team', 'training', 'benefits', 'cafeteria', 'office', 'parking', 'gym', 'onboarding'],
    'Construction': ['site', 'concrete', 'crane', 'welding', 'scaffolding', 'equipment', 'breakdown', 'delay', 'schedule', 'housekeeping'],
    'Management': ['budget', 'revenue', 'profit', 'client', 'stakeholder', 'strategy', 'goal', 'timeline', 'milestone']
}

# Critical Keywords for Severity
CRITICAL_WORDS = ['danger', 'emergency', 'critical', 'fail', 'crash', 'injury', 'stopped', 'rejected', 'corrupt', 'down', 'unstable', 'leak', 'malfunctioning']

def process_data():
    # --- 2. LOAD DATA FROM FILE ---
    input_file = 'ten_feedback_data.csv'
    try:
        df = pd.read_csv(input_file)
        print(f"✅ Successfully loaded '{input_file}'")
    except FileNotFoundError:
        print(f"❌ Error: '{input_file}' not found in this folder.")
        return

    # Initialize VADER
    nltk.download('vader_lexicon', quiet=True)
    sid = SentimentIntensityAnalyzer()

    # --- 3. ANALYSIS LOGIC ---
    def analyze_row(text, location):
        text_lower = str(text).lower()
        
        # A. Sentiment Score & Label
        sentiment_score = sid.polarity_scores(str(text))['compound']
        
        if sentiment_score >= 0.05:
            lbl = 'Positive'
            ind = 1
        elif sentiment_score <= -0.05:
            lbl = 'Negative'
            ind = -1
        else:
            lbl = 'Neutral'
            ind = 0

        # B. AI Predicted Category
        cat = "General"
        for k, v in CATEGORIES.items():
            if any(word in text_lower for word in v):
                cat = k
                break
        
        # C. Severity Score (1-5)
        sev = 1 # Default
        if lbl == 'Negative':
            sev = 3 # Base negative
            if cat in ['HSE', 'Construction', 'IT']: sev = 4 
            if any(c in text_lower for c in CRITICAL_WORDS): sev = 5 
        elif lbl == 'Positive':
            sev = 0 

        # D. Geography
        # Default to Paris if city is missing/unknown
        geo = GEO_MAP.get(location, GEO_MAP['Paris'])
        
        return pd.Series([
            geo['Country'], 
            geo['Lat'], 
            geo['Long'], 
            cat, 
            sev, 
            ind, 
            lbl
        ])

    # --- 4. APPLY & EXPORT ---
    print("⏳ Processing data rows...")
    
    new_cols = [
        'Country', 
        'Latitude', 
        'Longitude', 
        'AI_Predicted_Category', 
        'Severity_Score', 
        'Sentiment_Indicator', 
        'Sentiment_Label'
    ]
    
    # Run the function on every row
    df[new_cols] = df.apply(lambda row: analyze_row(row['Review_Text'], row['Location']), axis=1)

    output_filename = 'refined_ten_dashboard_data.csv'
    df.to_csv(output_filename, index=False)
    
    print(f"🎉 Success! Processed data saved to: '{output_filename}'")

if __name__ == "__main__":
    process_data()