<p align="center">
  <img src="LOGO-3.png" alt="LOGO" width="1200" height="500">
</p>

---

# Catcheater
In silico design for Project 'Catcheater'. A modular, tag-less quality-control (QC) system for *E. coli* to eliminate 'cheater' cells during protein production.

### 🎥 5-Minute Pitch Video: [https://drive.google.com/file/d/13TghXCWw8tjhXYNhB8or2Pou_nXmR0zS/view?usp=drive_link]

---

### 1. The Real Need

Large-scale protein production is chronically undermined by "Type-2 cheater" cells. These cells mutate to produce truncated or misfolded "junk" proteins. This is disastrous for two reasons:
1.  **They are toxic:** They trigger severe **proteotoxic stress**, consuming the cell's machinery.
2.  **They are fast:** They outgrow the "good" cells, causing the entire production batch to crash.

Current solutions are flawed. "Tag-based" systems require fusing tags to the protein, which violates the need for a pristine, tag-less product. "Transcript-linked" systems are "blind" to this failure, as the cheater cell *does* make the mRNA.

---

### 2. Our Solution: A Self-Policing Cellular Chassis

Project "CatchEater" is a complete *in silico* design for a modular, tag-less quality-control (QC) "chassis" built in *E. coli*.

Our system hijacks the cell's native stress pathways to execute a "kill" decision, while a novel **"translation-completion certificate"** protects the good, productive cells.

It is built on three core components:

1.  **A Dual-Sensor Logic Gate:** We re-wire the cell's native $\sigma^{32}$ (cytosolic) and $\sigma^{E}$ (envelope) stress sensors. This (Stress-OR-Stress) signal is fed into an AND-gate that also requires the "ProductionMode" (PM) key.
2.  **An Irreversible "Kill Latch":** A "cheater" cell (high stress, no antidote) activates a genomic **`flp` recombinase** (the Actuator). This Flp flips a permanent DNA switch (**`FRT-toxin-FRT`**), activating a lethal **`mazF` toxin** and irreversibly committing the cell to death.
3.  **A "Save" Signal (The Certificate):** Good cells are protected. The **`tetR` Antidote** gene is **translationally coupled** to the target protein's authentic stop codon. Only ribosomes that *finish* the protein can also make the Antidote. This `tetR` protein then binds to and *suppresses* the genomic kill-gate, granting the cell immunity.

---

### 3. How it Works: Kill vs. Save

This is the core logic of our system.

#### **Scenario A: The "Type-2 Cheater" (IS KILLED)**

(Stress is HIGH) + (Production is ON) + (Antidote is ABSENT) → Genomic Gate (P_hybrid) = ON → flp(ssrA) Actuator is produced → mazF Latch is FLIPPED → ***CELL DIES***

#### **Scenario B: The "Good Producer" (IS SAVED)**

Ribosome completes protein → "Certificate" is issued (Translational Coupling) → tetR Antidote is produced → Genomic Gate (P_hybrid) = OFF (Suppressed by Antidote) → ***CELL LIVES***

---

### 4. The Team

* AmirMohammad Cheraghali (Synthetic Biology and AI) - Sorbonne Université
* Sogand Azadeh (Genetics and Epigenetics) - Université Paris Cité
* AmirMahdi Karambakhsh (Systems and Synthetic Biology) - Université Paris-Saclay
* Fatemeh Sadat Mortazavi (Systems and Synthetic Biology) - Université Paris-Saclay

---
