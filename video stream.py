cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480)

pickle_in = open('model_trained_new.p', "rb")
model = pickle.load(pickle_in)
while True:
    success, frame = cap.read()
    
    img = np.asarray(frame)
    img = cv2.resize(img, (32,32))
    img = preprocess(img)
    
    img = img.reshape(1, 32,32,1)
    
    #predictions
    classIndex = int(model.predict_classes(img))
    
    
    predictions = model.predict(img)
    probVal = np.amax(predictions)
    print(classIndex, probVal)
    
    if probVal > 0.7:
        cv2.putText(frame, str(classIndex) + " " + str(probVal), (50,50), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0), 1)
    
   cv2.imshow("Classification", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break
