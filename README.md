<h1 align="center">🧬 Punnett Square Simulator</h1>

<p align="center">
    A command-line utility to simulate monohybrid genetic crosses and calculate resulting genotype probabilities.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A modular, zero-dependency Python CLI built to model monohybrid Punnett square crosses. It takes two parental genotypes, splits them into individual alleles, crosses every combination, and reports the resulting punnett square and/or genotype probabilities.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/punnett-square-simulator.git
cd punnett-square-simulator
```

## Usage

Pass two parental genotypes of the same monohybrid type. The tool crosses every allele combination and can print the punnett square, the genotype probabilities, or both.

```bash
python punnet-square.py Aa Aa --grid --probabilities
```

### Short Flags

The same arguments are available in short form:

```bash
python punnet-square.py Aa Aa -g -p
```

### Example Output

```
┌────┬────┬────┐
│    │ A  │ a  │
├────┼────┼────┤
│ A  │ AA │ Aa │
├────┼────┼────┤
│ a  │ Aa │ aa │
└────┴────┴────┘
Genotype   | Probability
-------------------------------------------
AA         | 25.0%
Aa         | 50.0%
aa         | 25.0%
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `p1` | *Genotype string* | *Required* | Genotype of parent 1 (e.g. `Aa`). |
| `p2` | *Genotype string* | *Required* | Genotype of parent 2 (e.g. `Aa`). |
| `-g`, `--grid` | *Flag* | `False` | Print the punnett square. At least one of `-g` or `-p` is required. |
| `-p`, `--probabilities` | *Flag* | `False` | Print the resulting genotype probabilities. At least one of `-g` or `-p` is required. |

## Feature Set

* **Allele Splitting:** Breaks each parental genotype string down into its individual alleles.
* **Full Cross Calculation:** Crosses every allele of parent 1 against every allele of parent 2 to build the punnett square.
* **Genotype Sorting:** Normalizes each resulting genotype by sorting dominant alleles before recessive ones.
* **Probability Calculation:** Tallies genotype frequencies across the square and converts them into percentages.
* **Grid Rendering:** Prints a clean, boxed punnett square with row and column allele headers.
* **Input Validation:** Rejects numerical characters in genotypes and requires both parents to share the same monohybrid type.

## License

MIT