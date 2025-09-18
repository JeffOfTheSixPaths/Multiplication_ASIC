# Introduction
- started this project as a way to explore an idea for my AP Physics C final project, but ended up working on it past the school year
- Uses Ohm's law to mimic AIMC and tries to speed up and increase energy efficiency for running neural networks.
- Made an engineering notebook which can be found [here on google docs](https://docs.google.com/document/d/1mhZI_8UCndxqVoLbu3UjTylmbxrZs0U-Nd4vj4mXka4/edit?tab=t.0)

# My implementation
- I found out about the concept of using Ohm's law to multiply from a veritasium video, and did my best to use that concept in my own way
- Typically memresistors are used to acheive variable resistance, but I used digital potentiometers.
- I trained a basic MNIST model and then loaded the weights onto the potentiometers to multiply the weights and inputs
- Ended up not reducing accuracy that much for larger models
- further details can be found in the engineering notebook including robustness to noise

![Graph of magitude of error for multiplying two numbers](https://media.discordapp.net/attachments/901256383289241693/1156055336252354621/image.png?ex=68ccc06e&is=68cb6eee&hm=b3027ca103528bb099292740103b266be380b0ecaea06f698859f04d8799c940&=&format=webp&quality=lossless)
