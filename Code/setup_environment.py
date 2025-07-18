import subprocess
import sys

#########################################################################################
#first things first; run this for setup library; after setup path on data.py and library.py for dataset
# ; now you are ready for some plot yeah!
def install_packages():
    try:
        # Install librabry from requirements.txt
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Tutte le librerie sono state installate correttamente!")
    except Exception as e:
        print(f"Si è verificato un errore durante l'installazione delle librerie: {e}")

if __name__ == "__main__":
    install_packages()
#########################################################################################