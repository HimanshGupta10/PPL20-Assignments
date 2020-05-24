#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>// for getting clock structure
#include <unistd.h>// for sleep() function

//pre defined structure present in <time.h> used for all time related stuff
struct tm * clocktime;

//function for constantly increasing seconds
void *functionsecs()
{
        while(1){
                sleep(1);
                clocktime->tm_sec +=1;
        }
}

//function for minutes increment
void *functionmins()
{
        while(1){
                sleep(60);
                clocktime->tm_min += 1;
                clocktime->tm_sec = 0;
        }        
}

//function for hourly increment
void *functionhrs()
{
        while(1){
                sleep(60*60);
                clocktime->tm_hour += 1;
                clocktime->tm_min = 0;
        }

}

//function for maintaining and printing digital clock after every second
void *clockfun(void *x){
        printf("Digital clock: \n");
        
        char shr[3] = {'\0'};
        char smin[3] = {'\0'};
        char ssec[3] = {'\0'};
        while(1){
                if(clocktime->tm_sec < 10){
                        sprintf(ssec, "0%d", clocktime->tm_sec);
                }
                else{
                        sprintf(ssec, "%d", clocktime->tm_sec);
                }
                if(clocktime->tm_min < 10){
                        sprintf(smin, "0%d", clocktime->tm_min);
                }
                else{
                        sprintf(smin, "%d", clocktime->tm_min);
                }
                if(clocktime->tm_hour < 10){
                        sprintf(shr, "0%d", clocktime->tm_hour);
                }
                else{
                        sprintf(shr, "%d", clocktime->tm_hour);
                }
                printf("\r%s:%s:%s", shr, smin, ssec);
        }
}
int main()
{
        pthread_t thread1, thread2, thread3, thread4; //thread ids
        
        //initializing the clock structure
        clocktime = (malloc(sizeof(struct tm))); 
        clocktime->tm_hour = 0;
        clocktime->tm_min = 0;
        clocktime->tm_sec = 0;
        
        //creating threads
        pthread_create( &thread1, NULL, &functionsecs, NULL);
        pthread_create( &thread2, NULL, &functionmins, NULL);
        pthread_create( &thread3, NULL, &functionhrs, NULL);
        pthread_create( &thread4, NULL, &clockfun, NULL);
        
        //joining threads
        pthread_join( thread1, NULL);
        pthread_join( thread2, NULL);
        pthread_join( thread3, NULL);
        pthread_join( thread4, NULL);
        
        return 0;
}
