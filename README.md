# nifi-deepspeech
Using Mozilla TensorFlow implementation of Baidu's Deep Speech


# Example Run with a Long Audio File

HW13125:DeepSpeech tspann$ ./runds.sh nifivid.wav
Loading model from file models/output_graph.pbmm
TensorFlow: v1.11.0-9-g97d851f04e
DeepSpeech: unknown
2018-12-10 11:23:03.697654: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
Loaded model in 0.0511s.
Loading language model from files models/lm.binary models/trie
Loaded language model in 16.1s.
Warning: original sample rate (44100) is different than 16kHz. Resampling might produce erratic speech recognition.
Running inference.
i am love gotitopracessorbut i ad it here will take a quick look and a tenet is adinit jomaanterfaceproutimeits pretty new it a still in blue beta until all one for which we leased to an one three one so this is a very early petitipeennofatouttheretheopenswourceanddarcumentetsimilaratotheattentirforaoneatyoucould see which is needs it drop in a directory will ben have this prebiltmonelticefterdownload it's all document pretty well drop it on here if hassan in a gin that image can come for em but you are all i we do over here i look where just grating or from picante give you some great deffreefotoesyou'llcingrabfromawebcameforwehaveonhereandfinallyumgravingsome grabbing some from some dew or traffic hammers again other sorcidytaottofwasto et in juice this could be coming from a device in the field where we you have a server night got a waste or run this just have to drop a model be don't have to install anything else which your getting from the job a code is everything you need but take a look at some of the results yeartotheetsontfolldeenisandnewdeda is is where this one came from his restored a directory as the files were getting undecided up to go the top five my one o which i down to de talk there we might be taken figure of will see what makes sense this is winning a couple of different things in air your tupersentagessaidboltiplybywahundred to get percentage as you get seehears kind you present from ability that there is a car the antis picture ever given back will casion to where it is in the image these may be all i might have to play with these factors to the boxes the rectangles are drawn perfectly again where in a rearlybeata at edcutcyyouknowafound the car found the bacca found the dog stop putting a boxes around their right but we have the deda for the seed we to start and were grabbing it for a couple of his things she could see here different probabilities the values what the classes are and all this tea we could pull out of here send it to track extracted his chasin will do that down here to put this led back the metadata and we got the process image the naga do whatever you want with it but to dive into the code real quick to kepeepaftheronealinsomeassistanceisconseeherethisis all eed to do tinsertenyoujobapiiforamerchneteiyou could see here to snatch shone on three one i not supposed to be production ready to west one for and as you could see her this one specific thing on here this is a morning on the back i don't know if we want to ah so if you're raingissouerhave to change after your vironment as one for line you just change it up if you need to as want to point that out of the carry a for good or process here isn't very similar to what we've done with the tenterflowone very similar i in fact took that is my starting point we've got a service get a flow file mature you pass in that model director he would can't do anything take that flow fillin coverted into bits and sennattuarclassofire so that is a very easy way to do that so we go into that and we could see okay what are we doing we think it monelpathfititoelagebyces et up on our single detection on it it see here ah we probably want to meet that size configure e run this i got five here we could do three or even just to top one how with the play ran with date mistecinfidurblfornalitonamdoingdowhitdaytodowegetbackout grote simple class o return this grabbed that way be let class name from ability in an the wee un the exit white ordinates with an height of got er lank which one i came in and next for it is we go to the frectodaprocesserathecould see for metthoseoutputtheminhisatributesindamostaritingontheeonthatimageputing ectanglesigisiftoget a couple of different colors there calycomplaywiththis for god any people i experience with doing old style ought or drawing or may be we use another library of still figure it out was the best way to draw a rectangle in job on an object the i sho talk to thee a field for gigas a re draw it in and one would done we get wet in out to that outwetstream said now will get that all those attributes than that back we've got a very simple test pity one who wants to collaborate quee a fork it out there and then we could just even had some more test of a minimum we definitely need more chester tester pretty minimal right now or is looking at this one method have got em out blood in an here i'm checking to see if it matches you know is a suppersonwhatstoprobabilitytatollgetoalowworachesting here obviously we should have cast wends new pass in a model even pass it in age to pass in a bad image you get the idea but once we get it back it still running this is an early release hopefully am keeping proving it not much to it but we now have of fully a patchy solution for ni five plus deep learning in one place thankyou
Inference took 287.790s for 1034.880s audio file.


Example Video used to extract audio:   https://www.youtube.com/watch?v=Q4dSGPvqXSA&t=0s&index=17&list=PL-7XqvSmQqfTSihuoIP_ZAnN7mFIHkZ_e


Setup

git clone https://github.com/mozilla/DeepSpeech
(Copy these shell and python scripts to that root directory)
pip3 install --upgrade deepspeech
Get the pretrained model 
wget -O - https://github.com/mozilla/DeepSpeech/releases/download/v0.3.0/deepspeech-0.3.0-models.tar.gz | tar xvfz -

I recommend Python 3.6.

