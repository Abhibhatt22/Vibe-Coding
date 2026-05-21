# 🤖 Agentic Campaign Optimization Engine

A **hands-on, interactive workshop application** demonstrating how AI agents can autonomously analyze marketing data, identify underperformers, optimize ad copy, and reallocate budgets for maximum ROI.

## 📋 Overview

This Streamlit application showcases the power of AI-driven marketing optimization through four interconnected modules:

1. **Campaign Dashboard** — Real-time performance monitoring across platforms and segments
2. **Anomaly Detection** — Automatic identification of underperforming campaigns
3. **Creative Optimization** — AI-generated ad copy variants for failing segments
4. **Budget Reallocation** — Data-driven budget recommendations with projected ROI impact

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. **Clone or navigate to the project:**
   ```bash
   cd agentic-campaign-optimizer
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate initial data (optional):**
   ```bash
   python utils/data_generator.py
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser:**
   Navigate to `http://localhost:8501`

---

## 📁 Project Structure

```
agentic-campaign-optimizer/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── pages/                          # Page modules
│   ├── __init__.py
│   ├── dashboard_page.py           # Campaign Dashboard
│   ├── anomaly_page.py             # Anomaly Detection
│   ├── creative_optimization_page.py   # Creative Optimization
│   └── budget_reallocation_page.py    # Budget Reallocation
│
├── utils/                          # Utility modules
│   ├── __init__.py
│   ├── data_generator.py           # Generate dummy marketing data
│   ├── agent_simulator.py          # AI agent simulation logic
│   └── helpers.py                  # Helper functions (charts, formatting)
│
├── data/                           # Data files
│   ├── marketing_campaigns.csv     # Generated campaign data (CSV)
│   └── marketing_campaigns.xlsx    # Generated campaign data (Excel)
│
└── .streamlit/                     # Streamlit configuration
    └── config.toml                 # Streamlit settings
```

---

## 📊 Features

### 1. Campaign Dashboard
- **Key metrics:** Total spend, conversions, CPA, CTR, ROAS
- **Interactive Plotly charts:** Spend vs Conversions, CPA by Platform, Segment Performance
- **Full campaign data table:** Browse all campaigns with filtering
- **Educational context:** Learn what each metric means

### 2. Anomaly Detection
- **Automatic flagging:** Segments with CPA > $50 or CTR < 0.5%
- **Visual highlighting:** Easy identification of problem areas
- **Detailed metrics:** Drill down into each underperformer
- **Summary statistics:** At-risk spend, number of flagged segments

### 3. Creative Optimization
- **AI analysis:** Diagnoses why each segment underperforms
- **Ad copy generation:** 3 AI-generated variants with different psychological angles
- **Angle diversity:** Problem-focused, Social proof, Direct benefit, etc.
- **Interactive buttons:** Approve, preview, or regenerate variants
- **Performance projections:** Expected CTR and CPA improvements

### 4. Budget Reallocation
- **Visual comparison:** Current vs recommended allocation
- **Detailed tables:** See exact budget changes per segment
- **Projected impact:** Estimated conversion lift with new allocation
- **Implementation guide:** Step-by-step checklist for deployment

---

## 🧠 How the AI Agent Works

### Data Analysis Flow
```
1. Load campaign data (500+ real-looking records)
   ↓
2. Calculate metrics: CTR, CPA, ROAS per segment
   ↓
3. Flag underperformers (CPA > $50 or CTR < 0.5%)
   ↓
4. Analyze root causes (audience, creative mismatch)
   ↓
5. Generate tailored solutions (new ad copy, budget shifts)
   ↓
6. Project impact (conversions, revenue lift)
```

### Intelligence Features
- **AgentSimulator class:** Simulates LLM analysis and ad copy generation
- **BudgetOptimizer class:** Calculates optimal budget allocation
- **Realistic data:** 500 marketing records with intentional underperformers
- **Educational messaging:** Explains what the agent is doing at each step

---

## 📊 Data Structure

The application uses a pandas DataFrame with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| Campaign_ID | string | Unique campaign identifier |
| Platform | string | Ad platform (Meta, Google, LinkedIn) |
| Audience_Segment | string | Target audience segment |
| Creative_Name | string | Ad creative variant name |
| Spend | float | Total ad spend ($) |
| Impressions | int | Total impressions |
| Clicks | int | Total clicks |
| Conversions | int | Total conversions |
| CTR | float | Click-Through Rate (%) |
| CPA | float | Cost Per Acquisition ($) |
| ROAS | float | Return on Ad Spend (multiplier) |
| Revenue | float | Revenue generated ($) |

### Example Data Distribution
- **500 total records**
- **65% high performers** (good CTR, low CPA, healthy ROAS)
- **35% intentional underperformers** (low CTR, high CPA, poor ROAS)
- **3-4 distinct underperforming segments** to flag and optimize

---

## 🎓 Workshop Learning Objectives

By using this application, participants will understand:

1. **AI in Marketing:** How agents can automate analysis and recommendations
2. **Data-Driven Decisions:** Moving beyond intuition to metrics
3. **Ad Optimization:** Creative and targeting improvements
4. **Budget Allocation:** Shifting spend from losers to winners
5. **AI Limitations:** Where human judgment is still essential

---

## ⚙️ Configuration

### Streamlit Settings
Edit `.streamlit/config.toml` to customize:
- Page layout (wide/centered)
- Color theme (light/dark)
- Font family
- Sidebar position

### Data Generation
To regenerate sample data, edit `utils/data_generator.py`:
```python
# Change number of records
df = generate_marketing_data(n_rows=1000)

# Adjust performance thresholds
cpa = np.random.uniform(8, 25)  # Good performers
cpa = np.random.uniform(65, 150)  # Bad performers
```

---

## 📚 Module Documentation

### `data_generator.py`
- **`generate_marketing_data(n_rows)`** — Creates synthetic marketing data
- **`save_data_to_files(df, output_dir)`** — Exports to CSV and Excel
- **`get_summary_stats(df)`** — Prints summary statistics

### `agent_simulator.py`
- **`AgentSimulator`** class — Simulates LLM analysis and ad generation
  - `analyze_segment_performance()` — Diagnoses underperformance
  - `generate_ad_variants()` — Creates 3 new ad copy options
  - `simulate_thinking()` — Shows thinking steps with spinner

- **`BudgetOptimizer`** class — Recommends budget reallocation
  - `recommend_budget_reallocation()` — Calculates optimal allocation

### `helpers.py`
- **Data functions:** `load_data()`, `get_underperformers()`
- **Chart functions:** `create_spend_vs_conversions_chart()`, `create_cpa_by_platform_chart()`, etc.
- **Format functions:** `format_currency()`, `format_percentage()`, `format_metric()`

---

## 🔧 Customization

### Add a New Audience Segment
Edit `utils/data_generator.py`:
```python
good_segments = [
    'Tech Bros 25-34',
    'Finance Professionals 35-50',
    # Add your segment here
]
```

### Change Performance Thresholds
Edit `pages/anomaly_page.py`:
```python
underperformers = get_underperformers(df, cpa_threshold=50, ctr_threshold=0.5)
#                                                     ^^                  ^^^
#                                          Change these values
```

### Customize Ad Variants
Edit `utils/agent_simulator.py`:
```python
variants_by_segment = {
    'Your Segment': [
        {
            'headline': 'Your headline here',
            'primary': 'Your ad copy here',
            'angle': 'Your angle name'
        },
        # ...
    ]
}
```

---

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Deploy to Streamlit Cloud
1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and connect your GitHub repo
4. Select branch and `app.py` as main file

### Deploy to Cloud Platforms
- **Heroku:** Use Procfile + requirements.txt
- **AWS:** Deploy with Gunicorn + Streamlit Server
- **Google Cloud:** Use Cloud Run with container

---

## 📈 Example Metrics

### Sample Output from Dashboard
```
Total Spend: $287,450
Conversions: 12,340
Average CPA: $23.28
Average CTR: 0.87%
Average ROAS: 2.14x

Underperforming Segments:
- Random Instagram Scrollers: CPA $128, CTR 0.24%
- Untargeted Banner Clickers: CPA $105, CTR 0.31%
- Misaligned Audience Group: CPA $87, CTR 0.42%

Budget Reallocation Impact:
Current Conversions: 12,340
Projected Conversions: 13,420 (+8.7%)
Estimated Revenue Lift: $235,600
```

---

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:
- [ ] Real LLM integration (OpenAI API, Claude, etc.)
- [ ] Real database backend (PostgreSQL, MongoDB)
- [ ] Multi-user support with authentication
- [ ] Historical trend analysis
- [ ] A/B test result tracking
- [ ] Integration with actual ad platforms (Meta, Google)

---

## 📝 License

MIT License — Free to use and modify for educational purposes.

---

## ❓ FAQ

**Q: Is this a real AI agent?**
A: No, it's a simulator for demonstration purposes. See "Future Enhancements" to integrate real LLMs.

**Q: Can I use real marketing data?**
A: Absolutely! Replace `data/marketing_campaigns.csv` with your own data (same schema).

**Q: How often should I run the agent?**
A: In production: weekly or after major spend changes. This demo shows the process once.

**Q: Why are some segments intentionally bad?**
A: To teach workshop attendees to *spot* problems. Real data often has subtle issues; this makes them obvious.

**Q: Can I integrate with Google Ads or Meta?**
A: Yes! You'd need to add API calls to pull real data and push recommendations back.

---

## 📞 Support

- 📧 For issues, create a GitHub issue
- 💬 For questions, check the FAQ above
- 📚 For Streamlit docs: https://docs.streamlit.io

---

## 🎉 Acknowledgments

Built as an educational tool to demonstrate:
- Autonomous AI agents in marketing
- Data-driven decision making
- Interactive Streamlit applications
- Python for marketing tech

Perfect for workshops, demos, and learning AI fundamentals in a business context!

---

**Happy optimizing! 🚀**
