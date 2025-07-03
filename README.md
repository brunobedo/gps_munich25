# GPS_Munich25

**Data Science and Sports Performance: A Bavarian–Latin American Initiative for Integrating GNSS, LPS, and Computer Vision Tracking in Team Sports Analysis**

This repository documents the collaborative efforts between the University of São Paulo (USP) and the Technical University of Munich (TUM) to develop and apply positional data analysis tools in team sports. The project promotes academic exchange, international workshops, and the development of open metrics and visualizations for performance analysis.

Certainly! Here’s how you can incorporate a “Hands-on Activity” section into your README, describing the five Google Colab notebooks, each with its direct link, short description, and a suggested flow for learners.

---

## 📝 Hands-on Activity: Positional Data Analysis in Team Sports

This repository provides a practical, step-by-step hands-on activity structured into five Colab notebooks. Each notebook targets a fundamental concept in positional tracking and team sports performance analysis. You can follow the sequence to build your understanding and skills in raw data processing, field calibration, and advanced spatial metrics.

**To participate, simply click each notebook link below and open in Google Colab.**

### 1. RAW GPS DATA CALIBRATION

[Open in Colab ▶️](https://colab.research.google.com/drive/1PXGyxd4NxlknCyrhddsM4g4GLnFoLO0K)
*Learn how to calibrate raw GPS data, align positional data with field dimensions, and correct for device drift/errors. This is a crucial first step to ensure reliable downstream analyses.*

---

### 2. Field Length & Width Estimation

[Open in Colab ▶️](https://colab.research.google.com/drive/1xiwUmwGlIxtj-iuj256HKKaTpyen7Bj9)
*Use calibrated data to estimate and validate field boundaries (length and width). These metrics are essential for spatial normalization and cross-session comparability.*

---

### 3. Effective Area

[Open in Colab ▶️](https://colab.research.google.com/drive/1v4jZPCroOsnmoVwBYBvh-SUOxumho4CG?usp=drive_link)
*Calculate the “effective area” occupied by a team during play using convex hull and other spatial metrics, quantifying team compactness or dispersion over time.*

---

### 4. Stretch Index

[Open in Colab ▶️](https://colab.research.google.com/drive/1xJPT6Q3YhVcobR034ltkItviQuea8oHw?usp=drive_link)
*Analyze the mean distance of each player to their team’s centroid (“stretch index”) as an indicator of tactical organization and team structure.*

---

### 5. Team Spread

[Open in Colab ▶️](https://colab.research.google.com/drive/1o8TMHEmSmq4SzHJSIcfefAJuN_GtgmX6?usp=drive_link)
*Compute the “team spread” by assessing pairwise distances between all team members, gaining insight into space occupation, stretching, and contraction patterns.*

---

**Recommended Workflow:**

* Start with Notebook 1 to calibrate and clean your positional data.
* Proceed through Notebooks 2–5 in order, as each metric builds on the previous steps.
* You are encouraged to experiment, visualize results, and adapt code to your own datasets.

---

**Have questions or want to share your results?**
Open an issue in this repository or reach out to the project team—collaboration and learning are at the heart of this initiative!

---

## 🚀 Getting Started

Clone the repository:
```bash
git clone https://github.com/brunobedo/gps_munich25.git
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Explore the folders:

* `/data` – Processed positional data for each sport
* `/examples` – Example notebooks and analysis scripts
* `/info` – Calibration files and testing protocols
* `/rawdata` – Raw Kinexon GPS data from field testing
* `/results` – Calculated metrics and visualizations
* `/src` – Source code for data processing and visualization

---

## 🗂 Repository Structure

```
gps_munich25/
│
├── data/               # Processed positional data (basketball, soccer, volleyball)
├── examples/           # Example scripts and notebooks
├── info/               # Calibration images and test protocols
│
├── rawdata/            # Raw Kinexon GPS data
│   ├── Kinexon GPS ELITE/
│   └── Kinexon GPS PRO/
│
├── results/            # Metrics and videos per analysis type and sport
│   ├── area/
│   ├── strechindex/
│   ├── teamspread/
│   └── width_length/
│       ├── basketball/
│       ├── soccer/
│       └── volleyball/
│
├── src/                 # Python source code for computation and analysis
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 📅 Itinerary & Timeline (2025 Highlights)

* **June, 2025** – Online Teaching Session 1 and 2 (USP)
* **July, 2025** – Technical Visit and Workshop at TUM (Munich, Germany)
* **October–December** – Online Teaching Sessions 3 and 4 (USP)
* **March, 2026** – Scientific Meeting and Workshop at USP (São Paulo, Brazil)
* **Throughout** – Collaborative development, data collection, and manuscript preparation

---

## 🏛 Facilities

* **USP**: School of Physical Education and Sport (São Paulo, Brazil)
* **TUM**: Department of Sport and Health Sciences (Munich, Germany)

---

## 👥 Project Team

### Principal Investigators

* **Prof. Dr. Bruno L. S. Bedo**, University of São Paulo (USP), Brazil
* **Prof. Dr. Tiago G. Russomanno**, Technical University of Munich (TUM), Germany

### Assistant Researchers

* **Prof. Dr. Paulo Roberto Pereira Santiago**, USP, Brazil
* **Prof. Dr. Daniel Link**, TUM, Germany
* **Prof. Dr. Felipe Arruda Moura**, State University of Londrina, Brazil

For more details, see the full project documentation in the `/docs` and `/info` folders.

---

## 🤝 Contributions

Contributions and collaboration are welcome. Please feel free to fork this repository, open issues, or submit pull requests. Suggestions for improving metrics, performance indicators, or visualizations are highly appreciated.

---

## 🙏 Acknowledgements

This project is supported by the **Bavarian Academic Center for Latin America (BAYLAT)** and involves collaboration with research initiatives funded by **FAPESP (São Paulo Research Foundation)** in Brazil.

We gratefully acknowledge the support of all institutions, researchers, and students involved.

---

## 📄 License

This project is licensed under the **GNU Lesser General Public License v3.0**.

If you use any part of the code, methodology, or data, please cite this repository or the associated publications. Let's collaborate and push the boundaries of sports performance research together!

---

## 📫 Contact
* **Prof. Dr. Bruno L. S. Bedo** — [bruno.bedo@usp.br](mailto:bruno.bedo@usp.br)
* **Prof. Dr. Paulo Roberto Pereira Santiago** — [paulosantiago@usp.br](mailto:paulosantiago@usp.br)
* **Prof. Dr. Tiago G. Russomanno** — [tiago.russomanno@tum.de](mailto:tiago.russomanno@tum.de)

```
