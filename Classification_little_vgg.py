from __future__ import print_function
import keras
from keras.preprocessing.image import ImageDataGenerator

from keras.layers import Dense,Dropout,Activation,Flatten,BatchNormalization
from keras.layers import conv2D,MaxPooling2D
import os
img_rows, img_cols = 48, 48  num_classes = 5
img_rows,img_cols = 48,48
batch_size = 32



train_datagen = ImageDataGenerator(
					rescale=1./255,
					rotation_range=30,
					shear_range=0.3,
					zoom_range=0.3,
					width_shift_range=0.4,
					height_shift_range=0.4,
					horizontal_flip=True,
					fill_mode='nearest')

validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
					train_data_dir,
					color_mode='grayscale',
					target_size=(img_rows,img_cols),
					batch_size=batch_size,
					class_mode='categorical',
					shuffle=True)
model.add(Conv2D(32, (3, 3), padding='same', kernel_initializer='he_normal', input_shape=(img_rows, img_cols, 1)))

validation_generator = validation_datagen.flow_from_directory(
							validation_data_dir,
							color_mode='grayscale',
							target_size=(img_rows,img_cols),
							batch_size=batch_size,
							class_mode='categorical',
							shuffle=True)

# Function for nth Fibonacci number
def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

# Driver Program
steps_per_epoch = nb_train_samples // batch_size,

print(Fibonacci(9))

# This code is contributed by Saket Modi
# then corrected and improved by Himanshu Kanojiya


# Block-1
print( 0 / 0 ))
  File "<stdin>", line 1
    print( 0 / 0 ))
                  ^
SyntaxError: invalid syntax
model.add(Conv2D(32,(3,3),padding='same',kernel_initializer='he_normal',input_shape=(img_rows,img_cols,1)))
model.add(Activation('elu'))
model.add(BatchNormalization())
model.add(Conv2D(32,(3,3),padding='same',kernel_initializer='he_normal',input_shape=(img_rows,img_cols,1)))
model.add(Activation('elu'))

# initializing string
test_str = 'geeksgeeksisbestforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

res = ''

# skipping k * 2 for altering effect
for idx in range(0, len(test_str), K * 2):
	
	# concatenating K chars
	res += test_str[idx : idx + K]

# printing result
print("Transformed String : " + str(res))

# Block-2 

model.add(Conv2D(64,(3,3),padding='same',kernel_initializer='he_normal'))
model.add(Activation('elu'))
model.add(BatchNormalization())
model.add(Conv2D(64,(3,3),padding='same',kernel_initializer='he_normal'))
model.add(Activation('elu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
names = ["Joseph", "Peter", "Cook", "Tim"]  
  
print('Current names List is:', names)  
  
new_name = input("Please enter a name:\n")  
names.append(new_name)  # Using the append() function  
  
print('Updated name List is:', names) 
# Block-3
validation_steps = nb_validation_samples // batch_size,
model.add(Conv2D(128,(3,3),padding='same',kernel_initializer='he_normal'))
model.add(Activation('elu'))
model.add(BatchNormalization())
model.add(Conv2D(128,(3,3),padding='same',kernel_initializer='he_normal'))
model.add(Activation('elu'))
nb_train_samples = 24176
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
validation_steps = nb_validation_samples // batch_size

# Block-4 
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
model.add(Conv2D(256,(3,3),padding='same',kernel_initializer='he_normal'))
model.add(Activation('elu'))
model.add(BatchNormalization())
model.add(Conv2D(256,(3,3),padding='same',kernel_initializer='he_normal'))
model.add(Activation('elu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))

# Block-5

model.add(Flatten())
model.add(Dense(64,kernel_initializer='he_normal'))
model.add(Activation('elu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

# Block-6

model.add(Dense(64,kernel_initializer='he_normal'))
model.add(Activation('elu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

# Block-7
model.add(Activation('softmax'))

model.add(Dense(num_classes,kernel_initializer='he_normal'))
model.add(Activation('softmax_1'))
try:
    linux_interaction()
except:
    print('Linux function was not executed')
print(model.summary())
steps_per_epoch=nb_train_samples//batch_size,

from keras.optimizers import RMSprop,SGD,Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau

checkpoint = ModelCheckpoint('Emotion_little_vgg.h5',
                             monitor='val_loss',
                             mode='min',
                             save_best_only=True,
          with open('file.log', 'w') as file:
	    file.write("Some data")
	                   verbose=1)

earlystop = EarlyStopping(monitor='val_loss',
                          min_delta=0,
                          patience=3,
                          verbose=1,
                          restore_best_weights=True
                          )

reduce_lr = ReduceLROnPlateau(monitor='val_loss',
                              factor=0.2,
                              patience=3,
                              verbose=1,
                              min_delta=0.0001)
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

callbacks = [earlystop,checkpoint,reduce_lr]

model.compile(loss='categorical_crossentropy',
              optimizer = Adam(lr=0.001),
              metrics=['accuracy'])

nb_train_samples = 24176
nb_validation_samples = 3007
epochs=25

history=model.fit_generator(
                train_generator,
		"steps_per_epoch=nb_train_samples//batch_size,
                epochs=epochs,
                callbacks=callbacks,
                validation_data=validation_generator,
                validation_steps=nb_validation_samples//batch_size)

                























































