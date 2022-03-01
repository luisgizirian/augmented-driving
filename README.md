# Augmented Driving

## Building trust towards self driving one step at a time.

The driver will be "augmented" by the real time information that will be supplied and colllected through our different sources. The feeding process will be done mixing visual and audio **cues, hints and suggestions** translated from real world. The driver will be fed with them, in order to enhance the decision process by gathering the right data at the right time whithout the effort that takes the driver doing it by itself. In other words, serving the info in a digestible fashion, without the effort. The driver can build trust on the automated system through repited positive validations, by comparing against the real-world.

We'll get there eventually, but it'll take baby steps (sources) to do so. The first source, will be Traffic Sign Recognition. For it, we'll try a hypothesis to mimic the human learning and inference processes. Shall such approach works, will suppose a leap forward for AGI (Artificisll General Intelligence) field evolution, bringing down significantly learning time and energy needs for some tasks.

### Our learning hypothesis: Light Learning for Object Recognition & Tracking

We humans, need a sample or two of an image, to learn a new object. Then, we’re able to recognize it in the wild, with little to no effort, after a brief consolidation period that regularly consists of light repetition, plus some trial and error.

#### General Objectives
* Learning from one (or just a few) sketch or sample
* Learn progressively through trial and error
* Minimum energy consumption when recognizing learned objects

#### Context (or Common Sense)
We map objects with a 3-dimensionality in mind. People has the “ability” to learn from a 2d sketch, and recognize a real 3d object instance (i.e. a Cow) when seen (i.e. in the Zoo). Laws of physics like gravity, are already internalized in our brains.

#### Stereoscopic vision [hypothesis]
Looks like a interesting addition, capable of abstracting objects from its context, to be recognized in isolation. If context is removed, and focusing can be a killer feature here, learning to recognize a learnt object in whatever Context, can become a no-brainer.

> On a second though, our ability to recognize from stills (imprinted photos) that are kind of flattened (2d) from their original form, shows us that learnt context may be powerfull enough to replace stereoscopic vision when not available.

#### Graph
we can recognize a plant, or a flower, without knowing the species. Maybe Light Learning refers to Generalized or Simple, and Deep Learning, refers to Specialized, and they’re complementary

#### Attribute Encoding learning approach
Describe from Attributes (is it Hard or Soft?), and complement with an Image or Two of the target. This technique looks to replace learning from many examples, in favor of deriving from what was learned (in a human-like fashion)

#### Sources:
* Traffic Sign Recognition
* Abide regulations while driving
* Surroundings (ie. other cars around us, pedestrians)
* Short, Mid, and Long term (ie. heading towards a visible twister)
* Anticipate actions (ie. Lights about to turn Red)

---

## Source #1: Traffic Sign Recognition

To test our hypothesis, we'll pick this challenge. At a high level, we're planning to learn from a sample or two + attributes [elaborate-here] (color, shape, disposition). At inference-time, coupling these with general cues such as Context, candidate abstraction (segmentation + stereoscopy) and graphing, may provide enough evidence to take an informed guess. It's a piramidal guessing approach, that shares phases.

* | Learning | Sample(s) | Attributes (dominant colors, shape, orientation) |
* | Inferencing (layer #1) | Graphing | Abstraction (segmentation or stereoscopy) |
* | Inferencing (layer #2) | Context (3-dimentionalizing, physics laws) |

From the sample pictogram (that a human could use as a source of truth for learning purposes - in a Driving Manual provided by your local institution), we may get some attributes that are useful for learning and later recognizing it in real world complex imagery that will be feeded. These attributes are: Shape, Primary color, orientation, compound shapes (ie. Stop All-way, Ramp Max Speed), relative size when related (ie. min - max speed limit in highway)
