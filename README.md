# Entropy-Based Cybersecurity Analysis

## Measuring Uncertainty and Predictability in Software Systems via the Entropy Rate of Random Walks on Weighted Graphs

This repository contains the implementation of a **Software Engineering project** that analyzes the predictability of cybersecurity event sequences using **graph-based modeling** and **information-theoretic metrics**.

User behavior is modeled as a **weighted directed graph**, interpreted as a **first-order Markov chain**, and analyzed using the **entropy rate** to quantify behavioral uncertainty and its evolution over time.

---

## 📌 Project Overview

Traditional security monitoring often relies on predefined rules or attack signatures. This project explores an alternative, **model-driven approach**, focusing on *how predictable system behavior is* rather than *what specific malicious patterns look like*.

The analysis combines:
- Graph theory
- Markov chains
- Information theory (entropy rate)
- Temporal behavioral analysis

to provide an interpretable and mathematically grounded framework for cybersecurity event analysis.

---

## 📊 Dataset

The project uses the **CERT Insider Threat Dataset**, a realistic research-grade dataset developed by the **Software Engineering Institute (SEI) at Carnegie Mellon University**, generated using the ExactData Dynamic Data Generator.

> ⚠️ **Important**  
> Due to licensing restrictions, raw dataset files are **not included** in this repository.  
> Only source code and derived results are provided.

**Primary dataset reference (DOI):**  
https://doi.org/10.1184/R1/12841247

---

## 🧠 Methodology

The analysis pipeline consists of the following steps:

1. **Log Preprocessing & Event Abstraction**  
   Raw log entries are mapped into abstract event types:
   - `LOGON`
   - `LOGOFF`
   - `HTTP_ACCESS`
   - `USB_CONNECT`
   - `USB_DISCONNECT`

2. **Timeline Construction**  
   Events from multiple sources are merged and sorted chronologically for each user.

3. **Graph Construction**  
   A **weighted directed graph** is built from consecutive event transitions.

4. **Transition Probability Estimation**  
   Edge weights are normalized to form a transition probability matrix.

5. **Stationary Distribution Computation**  
   The long-term behavior of the system is analyzed using power iteration.

6. **Entropy Rate Analysis**  
   - Per-state conditional entropy
   - Global entropy rate

7. **Temporal Analysis**  
   Entropy rates are compared across different time windows to analyze behavioral evolution.

8. **Visualization**  
   Graph structure, entropy contributions, and temporal trends are visualized.

---

## 🗂 Repository Structure
.
├── load_data.py              # Data loading and preprocessing
├── transitions.py            # Event mapping and graph construction
├── markov.py                 # Transition probabilities & stationary distribution
├── entropy.py                # Entropy rate and per-state entropy
├── temporal_analysis.py      # Temporal entropy comparison
├── visualization.py          # Graphs and plots
├── README.md                 # Project documentation
---

## ⚙️ Technologies Used

- **Python**
- `pandas` – data loading and preprocessing
- `numpy` – numerical computation
- `networkx` – graph modeling
- `matplotlib` – visualization

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/mirzoyanvahe/entropy-based-cybersecurity-analysis.git
cd entropy-based-cybersecurity-analysis

### 2. (Optional) Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate


### 3. Install dependencies
```bash
pip install pandas numpy networkx matplotlib

### 4. Run the analysis scripts
```bash
python transitions.py
python markov.py
python entropy.py
python temporal_analysis.py
python visualization.py

## 📈 Key Outcomes

- Construction of a **weighted directed graph** representing cybersecurity event transitions
- Estimation of **transition probabilities** and **stationary distribution**
- Computation of **per-state entropy** and **global entropy rate**
- Identification of **high-entropy behavioral bottlenecks**
- **Temporal entropy analysis** demonstrating behavioral stabilization over time
- Modular, interpretable, and reproducible software design suitable for academic analysis

---

## 🎓 Academic Context

This project was developed as part of a **Software Engineering course** and focuses on applying mathematically grounded techniques to cybersecurity data analysis.

Core concepts applied include:
- Markov chains
- Random walks on weighted directed graphs
- Entropy and entropy rate
- Temporal and comparative behavioral analysis

---

## 📜 License & Ethics

This repository does **not** contain raw dataset files and fully complies with the licensing terms of the **CERT Insider Threat Dataset**.

Only source code and derived results are provided for **educational and research purposes**.

---

## 👤 Author

**Vahe Mirzoyan**  
Cybersecurity / Computer Science  

🔗 GitHub: https://github.com/mirzoyanvahe 
🔗 LinkedIn: https://www.linkedin.com/in/VaheMirzoyan/
🔗 Website: https://vahemirzoyan.com
