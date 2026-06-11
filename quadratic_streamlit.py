import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ── Titre et description ──────────────────────────────────────────────────────
st.title("🔢 Résolution d'une équation du second degré")
st.markdown(
    r"""
    Trouve les racines de l'équation :
    $$ax^2 + bx + c = 0$$
    """
)

# ── Barre latérale : saisie des coefficients ─────────────────────────────────
st.sidebar.header("Coefficients")
a = st.sidebar.number_input("Coefficient a", value=1.0, step=0.1)
b = st.sidebar.number_input("Coefficient b", value=-3.0, step=0.1)
c = st.sidebar.number_input("Coefficient c", value=2.0, step=0.1)

# ── Calcul du discriminant ────────────────────────────────────────────────────
st.subheader("📐 Calcul")

if a == 0:
    st.error("⚠️ Le coefficient *a* ne peut pas être nul (ce n'est pas une équation du 2nd degré).")
else:
    delta = b**2 - 4 * a * c

    st.write(f"**Discriminant** : Δ = b² − 4ac = {b}² − 4×{a}×{c} = **{delta:.4f}**")

    if delta > 0:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        st.success(f"✅ Deux racines réelles : **x₁ = {x1:.4f}** et **x₂ = {x2:.4f}**")
        racines = [x1, x2]

    elif delta == 0:
        x0 = -b / (2 * a)
        st.info(f"ℹ️ Une racine double : **x₀ = {x0:.4f}**")
        racines = [x0]

    else:
        partie_reelle = -b / (2 * a)
        partie_imag   = np.sqrt(-delta) / (2 * a)
        st.warning(
            f"⚠️ Pas de racine réelle. Racines complexes :\n\n"
            f"**x₁ = {partie_reelle:.4f} + {partie_imag:.4f}i**\n\n"
            f"**x₂ = {partie_reelle:.4f} − {partie_imag:.4f}i**"
        )
        racines = []

    # ── Tracé de la parabole ─────────────────────────────────────────────────
    st.subheader("📈 Graphe de la parabole")

    x_center = -b / (2 * a)
    x = np.linspace(x_center - 5, x_center + 5, 400)
    y = a * x**2 + b * x + c

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x, y, color="steelblue", linewidth=2, label=f"f(x) = {a}x² + {b}x + {c}")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    # Marquage des racines réelles
    for r in racines:
        ax.plot(r, 0, "ro", markersize=8, zorder=5, label=f"x = {r:.3f}")

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Parabole y = ax² + bx + c")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_ylim(min(y) - 1, max(y) + 1)

    st.pyplot(fig)

# ── Pied de page ──────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("Exemple pédagogique Streamlit — Formation doctorants Génie des Procédés")
