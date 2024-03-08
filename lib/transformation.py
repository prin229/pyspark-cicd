#transforation file present here
def transforation(orderdf):
    return orderdf.groupby("status").count()