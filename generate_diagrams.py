import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import os

OUTPUT_DIR = "assets/diagrams"

def setup():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def save_fig(name):
    plt.savefig(os.path.join(OUTPUT_DIR, name), bbox_inches='tight', dpi=150, transparent=True)
    plt.close()

def draw_cartesian_plane():
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xticks(range(-5, 6))
    ax.set_yticks(range(-5, 6))
    save_fig('cartesian_plane.png')

def draw_right_triangle():
    fig, ax = plt.subplots(figsize=(5, 4))
    points = np.array([[0, 0], [4, 0], [4, 3], [0, 0]])
    ax.plot(points[:, 0], points[:, 1], 'b-', lw=2)
    ax.add_patch(patches.Rectangle((3.6, 0), 0.4, 0.4, fill=False, color='black'))
    ax.text(2, -0.4, 'a', fontsize=14)
    ax.text(4.2, 1.5, 'b', fontsize=14)
    ax.text(1.8, 1.7, 'c', fontsize=14)
    ax.axis('equal')
    ax.axis('off')
    save_fig('right_triangle.png')

def draw_unit_circle():
    fig, ax = plt.subplots(figsize=(5, 5))
    circle = plt.Circle((0, 0), 1, color='blue', fill=False, lw=2)
    ax.add_artist(circle)
    ax.axhline(y=0, color='k', linestyle='--')
    ax.axvline(x=0, color='k', linestyle='--')
    
    # Draw an angle
    angle = np.pi / 4
    x, y = np.cos(angle), np.sin(angle)
    ax.plot([0, x], [0, y], 'r-', lw=2)
    ax.plot(x, y, 'ro')
    
    # Draw arc
    arc = patches.Arc((0, 0), 0.4, 0.4, angle=0, theta1=0, theta2=45, color='r')
    ax.add_patch(arc)
    ax.text(0.25, 0.1, r'$\theta$', fontsize=14, color='red')
    
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')
    save_fig('unit_circle.png')

def draw_parabola():
    fig, ax = plt.subplots(figsize=(5, 5))
    x = np.linspace(-3, 3, 100)
    y = x**2
    ax.plot(x, y, 'b-', lw=2)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 9)
    save_fig('parabola.png')

def draw_normal_distribution():
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.linspace(-4, 4, 100)
    y = (1/np.sqrt(2*np.pi)) * np.exp(-0.5*x**2)
    ax.plot(x, y, 'b-', lw=2)
    ax.fill_between(x, y, alpha=0.2, color='blue')
    ax.axvline(x=0, color='r', linestyle='--', lw=1)
    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_xticklabels([r'$-3\sigma$', r'$-2\sigma$', r'$-\sigma$', r'$\mu$', r'$\sigma$', r'$2\sigma$', r'$3\sigma$'])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    save_fig('normal_distribution.png')

def draw_venn_diagram():
    fig, ax = plt.subplots(figsize=(5, 4))
    c1 = plt.Circle((-0.5, 0), 1.2, color='skyblue', alpha=0.5, lw=2, ec='blue')
    c2 = plt.Circle((0.5, 0), 1.2, color='salmon', alpha=0.5, lw=2, ec='red')
    ax.add_artist(c1)
    ax.add_artist(c2)
    ax.text(-1, 0, 'A', fontsize=16)
    ax.text(1, 0, 'B', fontsize=16)
    ax.text(0, 0, r'$A \cap B$', fontsize=12, ha='center', va='center')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')
    save_fig('venn_diagram.png')

def draw_bar_chart():
    fig, ax = plt.subplots(figsize=(5, 4))
    categories = ['A', 'B', 'C', 'D']
    values = [3, 7, 5, 2]
    ax.bar(categories, values, color='teal', alpha=0.7)
    ax.set_ylim(0, 8)
    ax.set_ylabel('Frequency')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_fig('bar_chart.png')

def draw_intersecting_lines():
    fig, ax = plt.subplots(figsize=(5, 4))
    # Line 1
    ax.plot([-2, 2], [-1, 1], 'k-', lw=2)
    # Line 2
    ax.plot([-1, 1], [1, -1], 'k-', lw=2)
    
    # Angles
    arc1 = patches.Arc((0, 0), 0.8, 0.8, angle=0, theta1=26, theta2=154, color='blue', lw=1.5)
    arc2 = patches.Arc((0, 0), 0.6, 0.6, angle=0, theta1=154, theta2=206, color='red', lw=1.5)
    ax.add_patch(arc1)
    ax.add_patch(arc2)
    
    ax.text(0, 0.6, r'$\alpha$', fontsize=14, color='blue', ha='center')
    ax.text(-0.5, 0, r'$\beta$', fontsize=14, color='red', ha='center', va='center')
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')
    save_fig('intersecting_lines.png')

def draw_inscribed_triangle():
    fig, ax = plt.subplots(figsize=(5, 5))
    circle = plt.Circle((0, 0), 1, color='black', fill=False, lw=2)
    ax.add_artist(circle)
    
    # Triangle points
    angles = [np.pi/2, 7*np.pi/6, 11*np.pi/6]
    pts = np.array([[np.cos(a), np.sin(a)] for a in angles])
    # Close triangle
    pts = np.vstack([pts, pts[0]])
    
    ax.plot(pts[:, 0], pts[:, 1], 'b-', lw=2)
    
    ax.plot(0, 0, 'ko') # Center
    ax.plot([0, pts[0][0]], [0, pts[0][1]], 'k--', lw=1)
    ax.text(0.1, 0.4, 'R', fontsize=12)
    
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')
    save_fig('inscribed_triangle.png')

if __name__ == '__main__':
    print("Setting up directory...")
    setup()
    print("Generating Cartesian Plane...")
    draw_cartesian_plane()
    print("Generating Right Triangle...")
    draw_right_triangle()
    print("Generating Unit Circle...")
    draw_unit_circle()
    print("Generating Parabola...")
    draw_parabola()
    print("Generating Normal Distribution...")
    draw_normal_distribution()
    print("Generating Venn Diagram...")
    draw_venn_diagram()
    print("Generating Bar Chart...")
    draw_bar_chart()
    print("Generating Intersecting Lines...")
    draw_intersecting_lines()
    print("Generating Inscribed Triangle...")
    draw_inscribed_triangle()
    print(f"All diagrams generated successfully in {OUTPUT_DIR}/")
