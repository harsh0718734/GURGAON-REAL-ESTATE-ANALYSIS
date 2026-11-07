# Gurgaon Real Estate Market Analysis

## About the Project

This project focuses on analysing the residential real estate market in Gurgaon, Haryana, to understand how property prices and valuations vary across different sectors, societies, and asset configurations.

Using Python, I explored a real-world Gurgaon property dataset and worked through 17 analytical questions. The analysis covers final listing prices, property dimensions (SqFt), rates per square foot, BHK configurations, property statuses, RERA regulatory approvals, and flagship builder brands.

The main objective was to explore the dataset, identify meaningful patterns, handle high-value luxury outliers, and understand real estate market trends through Exploratory Data Analysis (EDA) and data visualisations.

## Dataset Information

- **Dataset:** Gurgaon Residential Property Data
- **Total Records:** Airtight transactional records (Deduplicated logs)
- **Total Columns:** Alphanumeric market tracking metrics
- **Domain:** Real Estate / Property Valuation Hub
- **Analysis Type:** Exploratory Data Analysis (EDA)

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn

## Data Cleaning & Preparation

Before performing the analysis, I carried out the following data preparation steps to secure structural database integrity:

- Loaded the raw dataset using Pandas and inspected data structures.
- Standardised column headers by stripping white spaces and converting text into capitalized snake_case titles.
- Parsed alphanumeric punctuation anomalies inside `PRICE` and `RATE_PER_SQFT` columns, converting text traps into numeric floating-point fields.
- Cast property dimensions cleanly into uniform integer formats (`df['AREA'].astype(int)`).
- Executed strict cross-row deduplication filters to remove repeated listings and maintain a unique core.
- Standardised categorical text cases and engineered strict Boolean flags (`True` / `False`) to track RERA approval layers natively.

## Exploratory Data Analysis (17 Questions)

I explored different aspects of the Gurgaon real estate marketplace through 17 analytical questions.

### 1. Property Valuation & Locality Spreads

1. Identified the absolute costliest and cheapest residential flat listings circulating in the market registry using index-maximization logic.
2. Grouped rows by municipal locality blocks to isolate sectors commanding the highest and lowest average property prices.
3. Aggregated and sorted mean square-foot valuation scores to discover the highest and lowest rate-per-square-foot residential nodes.
4. Parsed property metrics across construction phases to track pricing means, medians, maximum benchmarks, and baselines.

### 2. Layout Configurations & Brand Equity

5. Evaluated property pricing variables (mean, median, max, min) cross-referenced against layout sizes and flat type specifications.
6. Analysed square-foot valuation rates across property types, sorting top performing categories by mean and median limits.
7. Evaluated regulatory risk thresholds to see how active RERA registration statuses directly affect median asset pricing.
8. Studied asset type parameters to map their direct impact on final residential property values.

### 3. Builder Performance & Structural Metrics

9. Analysed how development construction status cross-referenced with RERA certifications alters overall listing costs.
10. Isolated development society registries to determine clusters hosting the absolute lowest and highest individual listing prices.
11. Discovered the absolute cheapest and costliest property layout variations across mass-market segments.
12. Cross-examined median pricing spreads to determine whether flat type configurations break traditional valuation models.
13. Tracked the exact financial step-up in average property costs across escalating BHK layouts.
14. Isolated developer name strings to rank and isolate the top 10 highest-value real estate builders commanding top premiums.
15. Evaluated layout dimensions against rate parameters to observe if larger residential assets score higher square-foot valuations.
16. Filtered out multi-crore luxury outliers to map normal property area variables directly to final mass-market price listings.
17. Evaluated total market volume depth by counting listing frequencies across construction statuses based on RERA approvals.

## Project Visualizations & Analysis

### 1. Construction Status vs Pricing Breakdown

![STATUS VS PRICE](visualizations/STATUS%20VS%20PRICE.png)

This bar chart evaluates how construction statuses and RERA approvals dictate asset valuations. It highlights pricing margins across property phases hued by active regulatory tracks.

### 2. Asset Dimension Scaling vs Square-Foot Valuations

![AREA VS RATE PER SQFT](visualizations/AREA%20VS%20RATE%20PER%20SQFT.png)

This scatter plot tracks square-foot pricing behaviors against layout dimensions. An explicit filter was applied for properties below 20,000 SqFt to eliminate faulty axis compression and show the true cluster cleanly.

### 3. Property Area vs Price Distribution

![AREA VS PRICE](visualizations/AREA%20VS%20PRICE.png)

This visualization isolates mass-market pricing movements. It limits the plotting canvas to properties below 1.5 Crore INR, revealing a clear diagonal distribution trend by filtering out extreme ultra-luxury outliers.

### 4. Market Volume Breakdown: Status vs RERA Approvals

![STATUS VS RERA APPROVAL](visualizations/STATUS%20VS%20RERA%20APPROVAL.png)

This count plot displays the distribution of registered listings across different construction phases. It provides an immediate look at market volume allocations hued by active regulatory compliance.

## Key Learnings

Through this project, I gained practical experience in:

- Managing a real-world Indian real estate dataset with high outlier variance.
- Executed strict programmatic cleaning and feature engineering arrays using Pandas.
- Deploying statistical logic and lookup queries (`idxmax()` / `idxmin()`) to discover extreme property values.
- Preventing plot compression by introducing domain-specific data filtering scripts.
- Memory management protection by implementing safe canvas closure tools (`plt.close()`).
- Building clean data stories by pairing Matplotlib themes with Seaborn multi-variable hues.

## Conclusion

This project provided deep practical experience in parsing real-world Gurgaon real estate logs and evaluating factors associated with property pricing, brand equity, and regulatory compliance.

By executing a structured 17-question exploratory sequence, I successfully mapped valuation limits, identified flagship developer clusters, and exposed how RERA approvals insulate property valuations from mass-market drops.

The pipeline helped strengthen my core data engineering, analytical reporting, and visualization skills while demonstrating clean database standardization practices required for advanced production modeling.
