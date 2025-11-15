<p align="center">
  <img src="LOGO-3.png" alt="LOGO" width="1200" height="500">
</p>

---

# Catcheater
In silico design for Project 'CatchEater'. A modular, tag-less quality-control (QC) system for *E. coli* to eliminate 'cheater' cells during protein production.

### 🎥 5-Minute Pitch Video: [Link to your video presentation]

---

### 1. Project Idea & Motivation (The "Real Need")

Large-scale protein production is chronically undermined by "Type-2 cheater" cells. These cells mutate to produce truncated or misfolded "junk" proteins. This is disastrous for two reasons:
1.  **They are toxic:** They trigger severe **proteotoxic stress**, consuming the cell's machinery.
2.  **They are fast:** They outgrow the "good" cells, causing the entire production batch to crash.

Current solutions are flawed. "Tag-based" systems require fusing tags to the protein, which violates the need for a pristine, tag-less product. "Transcript-linked" systems are "blind" to this failure, as the cheater cell *does* make the mRNA.

### 2. Our Solution: A Self-Policing Cellular Chassis

Project "CatchEater" is a complete *in silico* design for a modular, tag-less quality-control (QC) "chassis" built in *E. coli*.

Our system hijacks the cell's native stress pathways to execute a "kill" decision, while a novel **"translation-completion certificate"** protects the good, productive cells.

It is built on three core components:

1.  **A Dual-Sensor Logic Gate:** We re-wire the cell's native $\sigma^{32}$ (cytosolic) and $\sigma^{E}$ (envelope) stress sensors. This (Stress-OR-Stress) signal is fed into an AND-gate that also requires the "ProductionMode" (PM) key.
2.  **An Irreversible "Kill Latch":** A "cheater" cell (high stress, no antidote) activates a genomic **`flp` recombinase** (the Actuator). This Flp flips a permanent DNA switch (**`FRT-toxin-FRT`**), activating a lethal **`mazF` toxin** and irreversibly committing the cell to death.
3.  **A "Save" Signal (The Certificate):** Good cells are protected. The **`tetR` Antidote** gene is **translationally coupled** to the target protein's authentic stop codon. Only ribosomes that *finish* the protein can also make the Antidote. This `tetR` protein then binds to and *suppresses* the genomic kill-gate, granting the cell immunity.

### 3. How it Works: Kill vs. Save (The "Demo")

This is the core logic of our system.

#### **Scenario A: The "Type-2 Cheater" (IS KILLED)**

(Stress is HIGH) + (Production is ON) + (Antidote is ABSENT) ↓ Genomic Gate (P_hybrid) = ON ↓ flp(ssrA) Actuator is produced ↓ mazF Latch is FLIPPED ↓ CELL DIES

#### **Scenario B: The "Good Producer" (IS SAVED)**

Ribosome completes protein ↓ "Certificate" is issued (Translational Coupling) ↓ tetR Antidote is produced ↓ Genomic Gate (P_hybrid) = OFF (Suppressed by Antidote) ↓ CELL LIVES

### 4. Repository Guide (Our "Designed Work")

This repository contains the complete "proof of work" and "designed work" for our hackathon submission.

* `📁 1_Proposal/`
    * Contains the full, detailed project proposal document.

* `📁 2_Construct_Designs/`
    * **Our core technical deliverable.** This folder contains the detailed genetic construct designs, including:
    * **Plasmid Map:** The annotated map for the swappable `pUC`-based application plasmid.
    * **Genomic Maps:** The detailed maps for the two genomic insertions into the **BL21(DE3)** chassis:
        1.  **The Decision Core** (at the `lacZ` locus).
        2.  **The Kill Latch** (at the `attTn7` locus).
    * **Part Sequences:** A file detailing the specific genetic parts (`P_hybrid`, `flp(ssrA)`, `tetR`, `mazF`, etc.).

* `📁 3_Protocols/`
    * The "clear direction towards PoC" as requested by the hackathon.
    * **`Chassis_Construction.md`:** A tailored protocol for the **CRISPR-Cas9** engineering workflow to build the chassis.
    * **`Proof_Of_Concept_Test.md`:** The full protocol for our (non-lethal) PoC experiment, which replaces the `mazF` toxin with a **GFP reporter** to validate the logic.

* `📁 4_Modeling/`
    * The *in silico* validation plan. This details the key parameters (`Ks`, `θ_latch`, `a`) for the ODE (Ordinary Differential Equation) model described in WP1.

* `📁 5_Presentation/`
    * Contains our final 5-minute video presentation and the slide deck used to create it.

### 5. The Team

* AmirMohammad Cheraghali - Sorbonne Université
* Sogand Azadeh - Université Paris Cité
* AmirMahdi Karambakhsh - Université Paris-Saclay
* Fatemeh Sadat Mortazavi - Université Paris-Saclay
