import matplotlib.pyplot as plt


# Plot fairness metrics
def plot_fairness_metrics(fairness_metrics):
    metrics = list(fairness_metrics.keys())
    values = list(fairness_metrics.values())
    
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Fairness Metrics')

    axs[0, 0].bar(metrics[0], values[0], color='blue')
    axs[0, 0].set_ylim(-1, 1)
    axs[0, 0].axhline(y=0.0, color='r', linestyle='--')
    axs[0, 0].set_title(metrics[0])

    axs[0, 1].bar(metrics[1], values[1], color='orange')
    axs[0, 1].set_ylim(-1, 1)
    axs[0, 1].axhline(y=0.0, color='r', linestyle='--')
    axs[0, 1].set_title(metrics[1])

    axs[0, 2].bar(metrics[2], values[2], color='green')
    axs[0, 2].set_ylim(-1, 1)
    axs[0, 2].axhline(y=0.0, color='r', linestyle='--')
    axs[0, 2].set_title(metrics[2])

    axs[1, 0].bar(metrics[3], values[3], color='purple')
    axs[1, 0].set_ylim(0, 2)
    axs[1, 0].axhline(y=1.0, color='r', linestyle='--')
    axs[1, 0].set_title(metrics[3])

    axs[1, 1].bar(metrics[4], values[4], color='red')
    axs[1, 1].set_ylim(0, 1)
    axs[1, 1].axhline(y=0.0, color='r', linestyle='--')
    axs[1, 1].set_title(metrics[4])

    fig.delaxes(axs[1, 2])  
    plt.tight_layout()
    plt.show()


# Plot comparative fairness metrics
def plot_comparative_fairness_metrics(fairness_metrics, fairness_metrics_transf):
    metrics = list(fairness_metrics.keys())
    values = list(fairness_metrics.values())
    values_bm = list(fairness_metrics_transf.values())

    groups = ['Original', 'Transformed']
    
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Comparative Fairness Metrics')

    axs[0, 0].bar(groups, [values[0],values_bm[0]], color=['blue', 'orange'])
    axs[0, 0].set_ylim(-1, 1)
    axs[0, 0].axhline(y=0.0, color='r', linestyle='--')
    axs[0, 0].set_title(metrics[0])

    axs[0, 1].bar(groups, [values[1],values_bm[1]], color=['blue', 'orange'])
    axs[0, 1].set_ylim(-1, 1)
    axs[0, 1].axhline(y=0.0, color='r', linestyle='--')
    axs[0, 1].set_title(metrics[1])

    axs[0, 2].bar(groups, [values[2],values_bm[2]], color=['blue', 'orange'])
    axs[0, 2].set_ylim(-1, 1)
    axs[0, 2].axhline(y=0.0, color='r', linestyle='--')
    axs[0, 2].set_title(metrics[2])

    axs[1, 0].bar(groups, [values[3],values_bm[3]], color=['blue', 'orange'])
    axs[1, 0].set_ylim(0, 2)
    axs[1, 0].axhline(y=1.0, color='r', linestyle='--')
    axs[1, 0].set_title(metrics[3])

    axs[1, 1].bar(groups, [values[4],values_bm[4]], color=['blue', 'orange'])
    axs[1, 1].set_ylim(0, 1)
    axs[1, 1].axhline(y=0.0, color='r', linestyle='--')
    axs[1, 1].set_title(metrics[4])

    fig.delaxes(axs[1, 2])  
    plt.tight_layout()
    plt.show()