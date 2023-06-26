def is_colab():
##### check of we are workin on Colab or Noteboook! 
#####-->> To change the paths accoring to that.
    try:
        import google.colab
        return True
    except ImportError:
        return False

if is_colab():
    print("Running in Google Colab")
else:
    print("Running in another notebook environment")