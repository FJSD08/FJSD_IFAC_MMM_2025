
# 🔍 Enhancing Operational Safety with Conformal Prediction in Soft Sensors

This repository contains the source code, datasets, and experimental results from the paper:

**“Enhancing Operational Safety with Conformal Prediction in Soft Sensors”**  
Francisco Diniz, Thomás Pinto, Saulo Matos, Jó Ueyama, Eduardo Luz, Gustavo Pessin

📌 **Conference**: 20th IFAC Symposium on Control, Optimization and Automation in Mining, Minerals and Metal Processing (MMM 2025)
📍 **Location**: Lima, Perú
📅 **Year**: 2025

---

## 🧠 Overview

This project presents a lightweight and interpretable method for **uncertainty quantification in soft sensors**, aimed at estimating ore mass flow rate in conveyor belts used in mining operations. The method enhances operational safety by combining:

- ✅ Linear regression models implemented in **PLCs**  
- 🎯 **Conformal Prediction (CP)** for adaptive prediction intervals  
- 🔁 **Sliding window** mechanism for online residual updates  
- 🧪 Statistical validation using **ANOVA** and **Tukey's HSD**

---

## 📈 Key Results

| Window Size | Interval Width (t/h) | Coverage (%) | Processing Time |
|-------------|----------------------|---------------|------------------|
| W100        | 286.62               | 95.3%         | < 0.1s           |
| W40         | 243.97               | 84.9%         | < 0.1s           |

✅ Real-time compatible for PLC-based environments  
🔄 Trade-off between robustness and responsiveness

---

## 📂 Repository Structure

```
├── data/                # Sample datasets (synthetic or anonymized)
├── src/                 # Core implementation (Python scripts or PLC logic)
│   ├── model/           # Linear regression + CP integration
│   ├── evaluation/      # Scripts for ANOVA and statistical testing
├── notebooks/           # Jupyter notebooks for experiments
├── results/             # Outputs and plots
├── README.md            # This file
└── requirements.txt     # Dependencies
```

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/soft-sensor-cp-plc.git
cd soft-sensor-cp-plc
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main script or open a notebook in `/notebooks/` to reproduce results.

---

## 📜 Citation

If you use this work, please cite:

```bibtex
@inproceedings{diniz2025cpsoftsensor,
  author    = {Francisco Diniz and Thomás Pinto and Saulo Matos and Jó Ueyama and Eduardo Luz and Gustavo Pessin},
  title     = {Enhancing Operational Safety with Conformal Prediction in Soft Sensors},
  booktitle = {20th IFAC Symposium on Control, Optimization and Automation in Mining, Minerals and Metal Processing (MMM 2025)},
  year      = {2025},
  address   = {Lima, Peru},
  publisher = {IFAC}
}
```
