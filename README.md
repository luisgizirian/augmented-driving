# Augmented Driving

## Building trust towards self driving, one step at a time.

The driver will become augmented by real time information comming from different sources that will be perceived and then fed to her. Feeding will be accomplished by **mixing visual and audio cues, hints and suggestions** translated from real world inferred events. The person will be able to focus on the main task, avoiding to scatter around, but at the same time, getting all the info from its surroundings in an organized and percievable fashion. Building trust on the automated system through repetitive validations by comparing fed results against the real-world.

We'll get there eventually, but it'll take baby steps (sources) to do so. The first source, will be Traffic Sign Recognition. For it, we'll give a try to a hypothesis on mimicking our species learning and inference processes. If such approach works, it will suppose a leap forward for AGI (Artificial General Intelligence) field evolution, bringing down significantly learning and inferencing, time and energy needs, for some scenarios or tasks.

### Our learning hypothesis: Light Learning for Object Recognition & Tracking

We humans, need a sample or two of an image (maybe as a lousy sketch), to learn a new object. Then, we’re able to recognize it in the wild, with little to no effort, after a brief consolidation period that regularly consists of light repetition to enforce the association, plus some trial and error.

#### General Objectives
* Learning from one (or just a few) sketch or sample
* Learn progressively through trial and error
* Minimum energy consumption when recognizing learned objects

#### Context (or Common Sense)
We map objects with a 3-dimensionality in mind. People has the “ability” to learn from a 2d sketch, and recognize a real 3d object instance (i.e. a Cow) when seen (i.e. in the Zoo). Laws of physics like gravity, are already internalized in our brains.

#### Stereoscopic vision [hypothesis]
Looks like a interesting addition, capable of abstracting objects from its context, to be recognized in isolation. If context is removed, and focusing can be a killer feature here, learning to recognize a learnt object in whatever Context, can become a no-brainer.

> On a second though, our ability to recognize from photos or drawings that are kind of flattened (2d) versions of their original form, gives us an indication that learnt context **may** be enough to compensate for stereoscopic vision where not available.

#### Graph
we can recognize a plant, or a flower, without knowing the species. Maybe Light Learning refers to Generalized or Simple, and Deep Learning, refers to Specialized, and they’re complementary

#### Attribute Encoding learning approach
Describe from Hard Attributes, and complement with an Image or Two of the target. This technique looks to replace learning from many examples, in favor of deriving from what was learned (in a human-like fashion)

#### Sources:
* Traffic Sign Recognition
* Abide regulations while driving
* Surroundings (ie. other cars around us, pedestrians)
* Short, Mid, and Long term (ie. heading towards a visible twister)
* Anticipate actions (ie. Lights about to turn Red)
* Lane Keeping, Adaptive Cruise Control (integrating with openpilot)

---

## Source #1: Traffic Sign Recognition

To test our hypothesis, we'll pick this challenge. At a high level, we're planning to learn from a sample or two + attributes [elaborate-here] (color, shape, disposition). At inference-time, coupling these with general cues such as Context, candidate abstraction (segmentation + stereoscopy) and graphing, may provide enough evidence to take an informed guess. It's a piramidal guessing approach, that shares phases.

* | Learning | Sample(s) | Attributes (dominant colors, shape, orientation) |
* | Inferencing (layer #1) | Graphing | Abstraction (segmentation or stereoscopy) |
* | Inferencing (layer #2) | Context (3-dimentionalizing, physics laws) |

From the sample pictogram (that a human could use as a source of truth for learning purposes - in a Driving Manual provided by your local institution), we may get some attributes that are useful for learning and later recognizing it in real world complex imagery that will be feeded. These attributes are: Shape, Primary color, orientation, compound shapes (ie. Stop All-way, Ramp Max Speed), relative size when related (ie. min - max speed limit in highway)
