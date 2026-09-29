import matplotlib.pyplot as plt
import networkx as nx

# ==========================================
# 1. CREAR EL GRAFO
# ==========================================

G = nx.Graph()

# Diego es el centro de la red
nodo_central = "Diego"

# Comunidades
familia = [
    "Mamá",
    "Papá",
    "Hermana",
    "Tío Alfredo",
    "Prima Lorena"
]

amigos_barrio = [
    "Pedro",
    "Jhoann",
    "Sofía",
    "Karen"
]

companeros_uni = [
    "Melissa",
    "Valentina",
    "Camilo",
    "Keithy"
]

# ==========================================
# 2. AGREGAR CONEXIONES CON DIEGO
# ==========================================

for persona in familia:
    G.add_edge(nodo_central, persona)

for persona in amigos_barrio:
    G.add_edge(nodo_central, persona)

for persona in companeros_uni:
    G.add_edge(nodo_central, persona)


# ==========================================
# 3. CONEXIONES DE LA FAMILIA
# ==========================================

conexiones_familia = [
    ("Mamá", "Papá"),
    ("Mamá", "Hermana"),
    ("Papá", "Hermana"),
    ("Mamá", "Tío Alfredo"),
    ("Tío Alfredo", "Prima Lorena"),
    ("Prima Lorena", "Hermana")
]

G.add_edges_from(conexiones_familia)


# ==========================================
# 4. CONEXIONES DE LOS AMIGOS
# ==========================================

conexiones_barrio = [
    ("Pedro", "Jhoann"),
    ("Jhoann", "Sofía"),
    ("Sofía", "Karen"),
    ("Pedro", "Karen")
]

G.add_edges_from(conexiones_barrio)


# ==========================================
# 5. CONEXIONES DE LA UNIVERSIDAD
# ==========================================

conexiones_uni = [
    ("Melissa", "Valentina"),
    ("Valentina", "Camilo"),
    ("Camilo", "Keithy"),
    ("Keithy", "Melissa"),
    ("Melissa", "Camilo")
]

G.add_edges_from(conexiones_uni)


# ==========================================
# 6. CONEXIONES ENTRE COMUNIDADES
# ==========================================

conexiones_puente = [
    ("Jhoann", "Melissa"),
    ("Hermana", "Keithy"),
    ("Karen", "Camilo")
]

G.add_edges_from(conexiones_puente)


# ==========================================
# 7. COLORES
# ==========================================

color_map = []

for node in G.nodes():

    if node == "Diego":
        color_map.append("#09FF00")       # Amarillo

    elif node in familia:
        color_map.append("#FF6B6B")       # Rojo

    elif node in amigos_barrio:
        color_map.append("#4D96FF")       # Azul

    elif node in companeros_uni:
        color_map.append("#6BC8CB")       # Verde


# ==========================================
# 8. POSICIONES MANUALES
# ==========================================

pos = {

    # --------------------------------------
    # CENTRO
    # --------------------------------------
    "Diego": (0, 0),

    # --------------------------------------
    # FAMILIA - PARTE SUPERIOR
    # --------------------------------------
    "Mamá": (-4.5, 3.2),
    "Papá": (-2.5, 4.0),
    "Hermana": (-0.5, 3.2),
    "Tío Alfredo": (-4.0, 1.7),
    "Prima Lorena": (-1.5, 1.7),

    # --------------------------------------
    # AMIGOS - PARTE DERECHA
    # --------------------------------------
    "Pedro": (4.8, 1.8),
    "Jhoann": (5.5, 0.2),
    "Sofía": (5.0, -1.8),
    "Karen": (3.2, -2.5),

    # --------------------------------------
    # UNIVERSIDAD - PARTE INFERIOR IZQUIERDA
    # --------------------------------------
    "Melissa": (-4.5, -1.7),
    "Valentina": (-2.5, -3.0),
    "Camilo": (-5.0, -3.2),
    "Keithy": (-6.0, -1.0)
}


# ==========================================
# 9. CREAR LA FIGURA
# ==========================================

plt.figure(figsize=(16, 11))


# ==========================================
# 10. SEPARAR TIPOS DE CONEXIONES
# ==========================================

# Conexiones de Diego
edges_diego = []

# Conexiones internas
edges_internas = []

# Conexiones entre comunidades
edges_puente = []

for edge in G.edges():

    a, b = edge

    if "Diego" in edge:
        edges_diego.append(edge)

    elif edge in conexiones_puente or (edge[1], edge[0]) in conexiones_puente:
        edges_puente.append(edge)

    else:
        edges_internas.append(edge)


# ==========================================
# 11. DIBUJAR CONEXIONES DE DIEGO
# ==========================================

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=edges_diego,
    width=2.5,
    edge_color="black",
    alpha=0.55
)


# ==========================================
# 12. DIBUJAR CONEXIONES INTERNAS
# ==========================================

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=edges_internas,
    width=1.8,
    edge_color="gray",
    alpha=0.65
)


# ==========================================
# 13. DIBUJAR CONEXIONES ENTRE COMUNIDADES
# ==========================================

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=edges_puente,
    width=2,
    edge_color="purple",
    style="dashed",
    alpha=0.8
)


# ==========================================
# 14. DIBUJAR NODOS
# ==========================================

nx.draw_networkx_nodes(
    G,
    pos,
    node_color=color_map,
    node_size=2300,
    edgecolors="black",
    linewidths=1.5
)


# ==========================================
# 15. RESALTAR DIEGO
# ==========================================

nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=["Diego"],
    node_color="#FFD700",
    node_size=3000,
    edgecolors="black",
    linewidths=2.5
)


# ==========================================
# 16. NOMBRES
# ==========================================

nx.draw_networkx_labels(
    G,
    pos,
    font_size=10,
    font_weight="bold"
)


# ==========================================
# 17. TÍTULO
# ==========================================

plt.title(
    "Grafo de Conexiones de Diego",
    fontsize=20,
    fontweight="bold",
    pad=20
)


# ==========================================
# 18. LEYENDA
# ==========================================

plt.scatter(
    [], [],
    c="#FFD700",
    s=120,
    label="Diego (Centro)"
)

plt.scatter(
    [], [],
    c="#FF6B6B",
    s=120,
    label="Familia"
)

plt.scatter(
    [], [],
    c="#4D96FF",
    s=120,
    label="Amigos del Barrio"
)

plt.scatter(
    [], [],
    c="#6BCB77",
    s=120,
    label="Universidad"
)

plt.plot(
    [],
    [],
    color="purple",
    linestyle="--",
    linewidth=2,
    label="Conexión entre comunidades"
)

plt.legend(
    title="Comunidades",
    loc="upper left",
    frameon=True,
    fontsize=10
)


# ==========================================
# 19. CONFIGURACIÓN FINAL
# ==========================================

plt.axis("off")

plt.xlim(-7, 7)
plt.ylim(-4.5, 5)

plt.tight_layout()

# ==========================================
# 20. MOSTRAR
# ==========================================

plt.show()