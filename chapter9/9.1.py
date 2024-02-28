    def update(self):
        rmin = 100
        rmax = 0
        thetamin =360
        thetamax=0
        for emote in self.emotions:
            theta = self.emotionAxis[emote]
            thetamax = min(theta,thetamax)
            thetamin = max(theta,thetamin)
            r = self.emotions[emote]
            rmin = max(rmin, r)
            rmax = max(rmax,r)
        stateR = (rmax-rmin)/ 2
        stateTheta = (thetamax-thetamin) / 2
        for emo in self.emotionAxis:
            thisAngle = self.emotionAxis[emo]
            if stateTheta > thisAngle
            myEmotion = emo
            break
        
        self.emostate = [stateTheta, stateR]
        if stateR < 55 and stateR > 45: 
            myEmotion = "neutral"
        self.emoText = myEmotion + " "+ str(stateR)
        print "Current Emotional State"  = myEmotion, stateR, stateTheta
        return
