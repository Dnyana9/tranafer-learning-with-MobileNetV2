import matplotlib.pyplot as plt

def plot_training_history_with_annotations(history, title='Training and Validation Accuracy & Loss', save_path=None):
    acc = history.history.get('accuracy')
    val_acc = history.history.get('val_accuracy')
    loss = history.history.get('loss')
    val_loss = history.history.get('val_loss')
    epochs = range(1, len(acc) + 1)

    # Get max accuracy and min loss with their epochs
    best_acc_epoch = val_acc.index(max(val_acc)) + 1
    best_acc = max(val_acc)

    best_loss_epoch = val_loss.index(min(val_loss)) + 1
    best_loss = min(val_loss)

    plt.figure(figsize=(14, 5))

    # Accuracy plot
    plt.subplot(1, 2, 1)
    plt.plot(epochs, acc, label='Training Accuracy', color='royalblue', linewidth=2)
    plt.plot(epochs, val_acc, label='Validation Accuracy', color='crimson', linewidth=2)
    plt.scatter(best_acc_epoch, best_acc, color='darkgreen')
    plt.text(best_acc_epoch, best_acc + 0.01, f'Best: {best_acc:.2f} (epoch {best_acc_epoch})',
             color='darkgreen', fontsize=10)
    plt.title('Accuracy Over Epochs', fontsize=14)
    plt.xlabel('Epochs', fontsize=12)
    plt.ylabel('Accuracy', fontsize=12)
    plt.legend()
    plt.grid(alpha=0.3)

    # Loss plot
    plt.subplot(1, 2, 2)
    plt.plot(epochs, loss, label='Training Loss', color='royalblue', linewidth=2)
    plt.plot(epochs, val_loss, label='Validation Loss', color='crimson', linewidth=2)
    plt.scatter(best_loss_epoch, best_loss, color='darkgreen')
    plt.text(best_loss_epoch, best_loss + 0.1, f'Lowest: {best_loss:.2f} (epoch {best_loss_epoch})',
             color='darkgreen', fontsize=10)
    plt.title('Loss Over Epochs', fontsize=14)
    plt.xlabel('Epochs', fontsize=12)
    plt.ylabel('Loss', fontsize=12)
    plt.legend()
    plt.grid(alpha=0.3)

    plt.suptitle(title, fontsize=16, weight='bold')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(f'{save_path}', dpi=300)
    plt.show()
