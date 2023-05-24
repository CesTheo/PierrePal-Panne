# import winreg

# # Chemin complet vers le fichier .exe
# exe_path = r'C:\chemin\vers\monfichier.exe'

# # Clé de registre à modifier
# key_path = r'Software\Microsoft\Windows\CurrentVersion\Run'

# # Ouvrir la clé de registre
# key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

# # Ajouter une valeur pour exécuter le fichier .exe au démarrage
# winreg.SetValueEx(key, 'MonExe', 0, winreg.REG_SZ, exe_path)

# # Fermer la clé de registre
# winreg.CloseKey(key)
