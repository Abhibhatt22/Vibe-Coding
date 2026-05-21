# 🚀 QUICK START GUIDE

## ✅ What Has Been Created

Your **Agentic Campaign Optimization Engine** is now ready to use! Here's what's included:

### 📁 Project Structure
```
agentic-campaign-optimizer/
├── app.py                    ← Main Streamlit application (RUN THIS)
├── requirements.txt          ← Python dependencies
├── README.md                 ← Full documentation
├── QUICK_START.md            ← This file
│
├── pages/                    ← Four main application pages
│   ├── dashboard_page.py     ← Campaign Dashboard
│   ├── anomaly_page.py       ← Anomaly Detection
│   ├── creative_optimization_page.py  ← Creative Optimization
│   └── budget_reallocation_page.py    ← Budget Reallocation
│
├── utils/                    ← Utility modules
│   ├── data_generator.py     ← Creates dummy data (500 marketing records)
│   ├── agent_simulator.py    ← AI agent logic for analysis & recommendations
│   └── helpers.py            ← Helper functions for charts & formatting
│
├── data/                     ← Marketing data
│   ├── marketing_campaigns.csv    ← CSV data export
│   └── marketing_campaigns.xlsx   ← Excel data export
│
├── .streamlit/
│   └── config.toml           ← Streamlit configuration
│
└── venv/                     ← Python virtual environment
```

---

## 🎯 How to Run the App

### Step 1: Activate Virtual Environment
```bash
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### Step 2: Launch Streamlit
```bash
streamlit run app.py
```

### Step 3: Open in Browser
The app will automatically open at: **http://localhost:8501**

---

## 📊 Features Overview

### **Page 1: Campaign Dashboard** 📊
- Real-time performance metrics (Spend, Conversions, CPA, CTR, ROAS)
- Interactive Plotly charts:
  - Spend vs Conversions by Platform
  - Average CPA by Platform
  - Segment Performance (CTR vs CPA scatter plot)
- Full campaign data table with 500 records

### **Page 2: Anomaly Detection** 🔍
- Automatically flags underperforming segments
- Filters: CPA > $50 or CTR < 0.5%
- Shows **3 intentionally bad performers** to optimize:
  - "Random Instagram Scrollers" (CPA: $104.60)
  - "Misaligned Audience Group" (CPA: $107.21)
  - "Untargeted Banner Clickers" (CPA: $104.34)
- Detailed metrics for each flagged segment
- AI recommendations for immediate action

### **Page 3: Creative Optimization** ✨
- Select an underperforming segment
- Click "Run AI Agent" button
- Agent generates:
  1. Analysis of *why* the creative is failing
  2. **3 new ad copy variants** with different psychological angles:
     - Pain-point focused
     - Social proof driven
     - Solution-oriented
- Approve/Preview/Regenerate buttons for each variant
- Projected performance improvements (CTR +2-3x, CPA -30-40%)

### **Page 4: Budget Reallocation** 💰
- Side-by-side comparison: Current vs Recommended budget
- Shows exact dollar shifts per segment
- Projects conversion lift with new allocation
- Implementation checklist (Today / This Week / Next 2 Weeks)
- Highlights underperformers being defunded
- Highlights top performers being boosted

---

## 📈 Dummy Data Details

### Generated Marketing Data (500 records)
- **Columns:** Campaign_ID, Platform, Audience_Segment, Creative_Name, Spend, Impressions, Clicks, Conversions, CTR, CPA, ROAS, Revenue
- **Platforms:** Meta, Google, LinkedIn
- **Good Segments (65% of data):**
  - Tech Bros 25-34 (CTR: 2.00%, CPA: $15.61)
  - Finance Professionals 35-50 (CTR: 2.09%, CPA: $16.97)
  - E-commerce Founders (CTR: 2.20%, CPA: $17.44)
  - SaaS Decision Makers (CTR: 1.95%, CPA: $16.88)
- **Bad Segments (35% of data) - Intentionally Underperforming:**
  - Random Instagram Scrollers (CTR: 0.26%, CPA: $104.60) ⚠️
  - Untargeted Banner Clickers (CTR: 0.25%, CPA: $104.34) ⚠️
  - Misaligned Audience Group (CTR: 0.24%, CPA: $107.21) ⚠️

### Summary Stats
- Total Spend: **$1,508,220**
- Total Conversions: **67,256**
- Average CPA: **$47.70**
- Average CTR: **1.16%**
- Average ROAS: **12.08x**

---

## 🤖 How the AI Agent Works

### AgentSimulator Class
```python
agent = AgentSimulator()

# 1. Analyze why a segment is underperforming
analysis = agent.analyze_segment_performance(
    segment_name, cpa, ctr, spend, conversions
)

# 2. Generate 3 new ad copy variants
variants = agent.generate_ad_variants(segment_name)
```

### BudgetOptimizer Class
```python
optimizer = BudgetOptimizer()

# Recommend optimal budget reallocation
recommendations = optimizer.recommend_budget_reallocation(df)
# Returns:
# - current_allocation
# - recommended_allocation
# - projected_conversions
# - improvement_pct
```

---

## 🎓 Use Cases for This Workshop

1. **Show AI-Powered Analysis:** Demonstrate how agents can autonomously scan data and find problems
2. **Creative Optimization:** Show how AI can generate targeted ad copy variants
3. **Budget Optimization:** Visualize how data-driven allocation beats intuition
4. **Interactive Learning:** Hands-on tool to explore AI capabilities in marketing
5. **Decision Support:** Show how humans + AI = better decisions than either alone

---

## 🔧 Customization Tips

### Add Your Own Data
Replace `data/marketing_campaigns.csv` with your own marketing data (same column schema)

### Change Thresholds
Edit `pages/anomaly_page.py`:
```python
underperformers = get_underperformers(df, cpa_threshold=50, ctr_threshold=0.5)
```

### Add Real LLM Integration
In `utils/agent_simulator.py`, replace simulation with real API calls:
```python
from openai import OpenAI
client = OpenAI(api_key="YOUR_KEY")
response = client.chat.completions.create(...)
```

### Customize Ad Variants
Edit `utils/agent_simulator.py` to change the `variants_by_segment` dictionary with your own angles

---

## 📚 Key Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit app - navigation & session management |
| `utils/data_generator.py` | Generates 500 realistic marketing records with intentional underperformers |
| `utils/agent_simulator.py` | AI agent logic (analysis + ad generation) & budget optimizer |
| `utils/helpers.py` | Helper functions for charts, formatting, data filtering |
| `pages/dashboard_page.py` | Campaign performance overview & charts |
| `pages/anomaly_page.py` | Automatic underperformer detection |
| `pages/creative_optimization_page.py` | AI-generated ad copy variants |
| `pages/budget_reallocation_page.py` | Budget shift recommendations |

---

## 🐛 Troubleshooting

### Issue: "No module named 'streamlit'"
**Solution:** Activate venv and install packages:
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: "Marketing data not found"
**Solution:** Generate the data:
```bash
python utils/data_generator.py
```

### Issue: App runs but pages don't load
**Solution:** Make sure you're in the project root directory when running `streamlit run app.py`

---

## 📞 Next Steps

1. **Run the app:** `streamlit run app.py`
2. **Explore all 4 pages** using the sidebar navigation
3. **Click "Run AI Agent"** on the Creative Optimization page to see it in action
4. **Check the Budget Reallocation** to see the projected impact
5. **Review README.md** for full documentation

---

## 🎉 You're All Set!

Your Agentic Campaign Optimization Engine is ready for your workshop. The app features:

✅ Interactive dashboard with Plotly charts
✅ Automatic anomaly detection
✅ AI-powered creative optimization
✅ Data-driven budget recommendations
✅ 500 realistic marketing records with intentional underperformers
✅ Educational markdown explaining each step
✅ Fully commented, production-ready code

Happy optimizing! 🚀
