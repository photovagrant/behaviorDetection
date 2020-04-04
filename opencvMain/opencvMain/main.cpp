//
//  main.cpp
//  testopencv
//
//  Created by assam on 2020/3/26.
//  Copyright © 2020 assam. All rights reserved.
//

//Uncomment the following line if you are compiling this code in Visual Studio
//#include "stdafx.h"

#include <opencv2/opencv.hpp>
#include <iostream>
#include <unistd.h>
using namespace cv;
using namespace std;

int checkVideoStatus(VideoCapture cap)
{
    if (cap.isOpened() == false)
    {
        cout << "Cannot open the video file" << endl;
        cin.get(); //wait for any key press
        return -1;
    }
    return 0;
}


int main(int argc, char* argv[])
{
    //open the video file for reading
    //VideoCapture cap1("/Users/assam/Desktop/弓的知識上長下短為什麼.mov");
    //VideoCapture cap2("/Users/assam/Desktop/弓的知識上長下短為什麼.mov");

    //VideoCapture cap1("rtsp://admin:admin@172.19.148.68/play1.sdp");
    //VideoCapture cap1("/Users/assam/Desktop/弓的知識上長下短為什麼.mov");
    VideoCapture cap1(0); // open the default camera
    if(!cap1.isOpened()) { // check if we succeeded
        std::cout << "no capture device1 :(\n";
        return -1;
    }
    if( checkVideoStatus(cap1))  { return 0 ;};
    VideoCapture cap2(1); // open the default camera
    if(!cap2.isOpened()) { // check if we succeeded
        std::cout << "no capture device2 :(\n";
        return -1;
    }
    //VideoCapture cap2("/Users/assam/Desktop/弓的知識上長下短為什麼.mov");
    //VideoCapture cap2("rtsp://admin:admin@172.19.148.128/play1.sdp");
    if( checkVideoStatus(cap2))  { return 0 ;};
    //VideoCapture cap(0);
    // // if not success, exit program
    // if (cap.isOpened() == false)
    // {
    //  cout << "Cannot open the video file" << endl;
    //  cin.get(); //wait for any key press
    //  return -1;
    // }
    
    
    //Uncomment the following line if you want to start the video in the middle
    //cap.set(CAP_PROP_POS_MSEC, 300);
    
    //get the frames rate of the video
    double fps = cap1.get(CAP_PROP_FPS);
    cout << "Frames 1 per seconds : " << fps << endl;
    
    fps = cap2.get(CAP_PROP_FPS);
    cout << "Frames 2 per seconds : " << fps << endl;
    
    vector<Mat> images;
    
    String window_name = "My First Video";
    
    namedWindow(window_name, WINDOW_NORMAL); //create a window
    bool bSuccess = false;
    Mat tmpframe,frame1,frame2;
    Mat DispImage = Mat::zeros(Size(1920,1080), CV_8UC3);
    Rect ROI1(20, 0, 640, 360);
    Rect ROI2(60, 500, 640, 360);
    Mat tmp;
    while (true)
    {
        
        bSuccess = cap1.read(frame1); // read a new frame from video
        if (bSuccess == false)
        {
            cout << "Found the end of the video frame1" << endl;
            break;
        }
        bSuccess = cap2.read(frame2); // read a new frame from video
        if (bSuccess == false)
        {
            cout << "Found the end of the video framw2" << endl;
            break;
        }

        resize(frame1,tmpframe,Size(640,360));
        tmpframe.copyTo(DispImage(ROI1));
        resize(frame2,tmpframe,Size(640,360));
        tmpframe.copyTo(DispImage(ROI2));
        
        
        //Breaking the while loop at the end of the video
        
        
        //show the frame in the created window
        imshow(window_name, DispImage);
        usleep(1);
        //imshow(window_name, frame2);
        //wait for for 10 ms until any key is pressed.
        //If the 'Esc' key is pressed, break the while loop.
        //If the any other key is pressed, continue the loop
        //If any key is not pressed withing 10 ms, continue the loop
        
        if (waitKey(1) == 27)
        {
            cout << "Esc key is pressed by user. Stoppig the video" << endl;
            break;
        }
    }
    
    return 0;
    
}
