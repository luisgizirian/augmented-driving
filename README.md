# Augmented Driving

We'll get there eventually, but it'll take baby steps (sources) to do so. The first source, will be Traffic Sign Recognition. For it, we'll try a hypothesis to mimic the human learning and inference processes. Shall such technique work, will suppose a leap forward for AGI (Artificisll General Intelligence) field evolution, bringing down significantly learning time and energy needs.

## Our learning hypothesis: Light Learning for Object Recognition & Tracking

We humans, need a sample or two of an image, to learn a new object. Then, we’re able to recognize it in the wild, with little to no effort, after a brief consolidation period that regularly consists of light repetition, plus some trial and error.

## Building trust towards self driving one step at a time.

The driver will be "augmented" by the real time information that will be supplied and colllected through our different sources. The feeding process will be done mixing visual and audio cues, so the driver will be fed with it, in order to enhance the decision process by gathering the right data at the right time.


### Main goals
* Learning from one (or just a few) sketch or sample
* Learn progressively through trial and error
* Minimum energy consumption when recognizing learned objects

### Context or Common Sense
Laws of physics - Gravity basically
3 Dimensionality
We map objects with a 3D dimensionality in mind. We “have” the “ability” to learn from a 2d sketch, and recognize a real 3d object instance (i.e. a Cow) when seen (i.e. in the Zoo).

### Stereoscopic vision [hypothesis]
Looks like a cornerstone to abstract an object from its context, to be recognized in isolation. There’s a say that, thru Deep Learning training, recognizing a Cow, posing in a Beach, requires samples provided at training time. But if context is removed, and focusing can be a killer feature here, learning to recognize a Cow in whatever Context, can become a no-brainer.

> On a second though, our ability to recognize from stills (imprinted photos) that are kind of flattened (2d) from their original form, shows us that learnt context may be powerfull enough to replace stereoscopic vision when not available.

### Graph
we can recognize a plant, or a flower, without knowing the species. Maybe Light Learning refers to Generalized or Simple, and Deep Learning, refers to Specialized, and they’re complementary

### Attribute Encoding approach
Describe from Attributes (is it Hard or Soft?), and complement with an Image or Two of the target. This technique looks to replace learning from many examples, in favor of deriving from what was learned (in a human-like fashion)

---
## Traffic Sign recognition
To test our hypothesis, we'll pick this challenge, that's a step on a much bigger one: Augmented Driving.

### Augmented Driving
The reason behind it, is to serve as a step for Autonomous Driving. Closing the trust gap that blocks us from delegating a life or death task to a machine. By using Augmentation to show what the computer sees, considers, but leaving the human in the loop, to make decisions with the information and hints that the computer provides in real time.

Scenarios:
* Traffic Sign recog
* Abide regulations while driving
* Surroundings (ie. other cars around us, pedestrians)
* Short, Mid, and Long term (ie. heading towards a visible twister)
* Anticipate actions (ie. Lights about to turn Red)

### Traffic Sign recognition
At a high level, we're planning to learn from a sample + attributes.

From the sample pictogram (that a human could use as a source of truth for learning purposes), we may get some attributes that are useful for learning and later recognizing it in real world complex imagery that will be feeded. These attributes are: Shape, Primary color, orientation, compound shapes (ie. Stop All-way, Ramp Max Speed), relative size when related (ie. min - max speed limit in highway)
