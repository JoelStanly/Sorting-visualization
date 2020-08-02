import pygame
import random
import time

pygame.init()
screen =pygame.display.set_mode((500,550))
#Handlings
def starter(li):
    global allow
    allow=False
    done_drawer(li)

def ender(li):
    done_drawer(li)
    back_button()
    pygame.display.update()

def eventhandling():
    global allow,screen,sorts,buttonDimensions
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and allow==True:
                mouse=pygame.mouse.get_pos()
                for i in buttonDimensions:
                    if(mouse[0]>=i[0] and mouse[0] <=i[2] and mouse[1]>=i[1] and mouse[1] <=i[3]):
                        li=listmaker()
                        eval(sorts[buttonDimensions.index(i)].replace(" ","_")+f"({li})")
            if event.type == pygame.MOUSEBUTTONDOWN and allow==False:
                mouse=pygame.mouse.get_pos()
                if(mouse[0]>=200 and mouse[0]<=300 and mouse[1]>=0 and mouse[1]<=50):
                    running=False
                    main_menu()
            if event.type==pygame.QUIT:
                running=False

#Draw Function
def back_button():
    myfont=pygame.font.SysFont("kokila",36)
    x=200
    y=0
    width=100
    height=50
    pygame.draw.rect(screen,(200,200,200),(x+2,y+3,width,height))
    pygame.draw.rect(screen,(0,0,0),(x,y,width,height))
    label=myfont.render("Back",1,(255,255,255))
    label_rect=label.get_rect()
    label_rect.center=((x+(width//2),y+(height//2)))
    screen.blit(label,label_rect)

def done_drawer(list1):
    screen.fill((200,200,200))
    for j in range(len(list1)):
        pygame.draw.rect(screen,(21,21,21),(j*5,550-list1[j],5,list1[j]))
    pygame.display.update()
    time.sleep(1)

def drawer(so,li,i,k=-1,rev=0):
    screen.fill((200,200,200))
    myfont=pygame.font.SysFont("kokila",36)
    x=200
    y=0
    width=100
    height=50
    label=myfont.render(so,1,(21,21,21))
    label_rect=label.get_rect()
    label_rect.center=((x+(width//2),y+(height//2)))
    screen.blit(label,label_rect)
    for j in range(len(li)):
        if j in i:
            pygame.draw.rect(screen,(255,0,100),(j*5,550-li[j],5,li[j]))
        if (j<=k and rev==0) or (j>=k and rev==1):
            pygame.draw.rect(screen,(21,21,21),(j*5,550-li[j],5,li[j]))
        elif j not in i:
            pygame.draw.rect(screen,(0,100,255),(j*5,550-li[j],5,li[j]))
        

    pygame.display.update()
    time.sleep(.02)

#Making List
def listmaker():
    list1=[]

    while len(list1)<100:
        num=random.randint(1,500)
        if num not in list1:
            list1.append(num)
    done_drawer(list1)
    return list1


#Pancake Sort
def flip(li,i,cur):
    start =0
    while start<i:
        temp=li[start]
        li[start]=li[i]
        li[i]=temp
        start+=1
        i-=1
        drawer("Pancake Sort",li,[start,i],cur,1)

def findMax(li,n):
    mi=0
    for i in range(n):
        if li[i]>li[mi]:
            mi=i
    return mi

def PanCake_Sort(li):
    starter(li)
    curr_size=len(li)
    
    while curr_size>1:
        mi=findMax(li,curr_size)

        if mi!=curr_size-1:
            flip(li,mi,curr_size-1)
            flip(li,curr_size-1,curr_size-1)
        curr_size-=1
    ender(li)

#Comb Sort
def getNextGap(gap):
    gap=(gap*10)//13
    if gap<1:
        return 1
    return gap
def Comb_Sort(li):
    starter(li)
    n=len(li)
    gap=n
    swap=True
    while gap!=1 or swap==True:
        gap=getNextGap(gap)
        swap=False
        
        for i in range(0,n-gap):
            if li[i]>li[i+gap]:
                li[i],li[i+gap]=li[i+gap],li[i]
                drawer("Comb Sort",li,[i,i+gap])
                swap=True
    ender(li)

#Tim Sort
def Tim_Sort(li):
    starter(li)
    n=len(li)
    run=32
    output=[]
    for i in range(0,n,run):
        output.extend(Insertion_Sort(li[i:min((i+32),(n))]))
    size=run
    li=output
    while size<n:
        for left in range(0,n,2*size):
            mid=left+size-1
            right=min((left+2*size-1),(n-1))
            merge(li,left,mid,right)
        size=2*size
    ender(li)

#Bogo Sort
def shuffle(li):
    n=len(li)
    for i in range(n):
        r=random.randint(0,n-1)
        li[i],li[r]=li[r],li[i]
        drawer("Bogo Sort",li,[i,r])

def is_sorted(li):
    n=len(li)
    for i in range(n-1):
        drawer("Bogo Sort",li,[i,i+1])
        if li[i]>li[i+1]:
            return False
    return True

def Bogo_Sort(li):
    starter(li)
    while (is_sorted(li)==False):
        shuffle(li)
    ender(li)

#Shell Sort
def Shell_Sort(li):
    starter(li)
    n=len(li)
    interval=n//2
    while interval>0:
        for i in range(interval,n):
            temp=li[i]
            j=i
            while j>=interval and li[j-interval]>temp:
                li[j]=li[j-interval]
                j-=interval
                drawer("Shell Sort",li,[i],j)
            li[j]=temp
        interval//=2
    ender(li)

#Radix Sort
def CountingSort(li,place):
    size=len(li)
    output=[0]*size
    count=[0]*10

    for i in range(0,size):
        index=li[i]//place
        count[index%10]+=1
    for i in range(1,10):
        count[i]+=count[i-1]

    i=size-1
    while i>=0:
        index=li[i]//place
        output[count[index%10]-1]=li[i]
        drawer("Radix Sort",output,[index])
        count[index%10]-=1
        i-=1
    for i in range(size):
        li[i]=output[i]
        drawer("Radix Sort",output,[i],i)


def Radix_Sort(li):
    starter(li)
    max_element=max(li)
    place=1
    while max_element//place >0:
        CountingSort(li,place)
        place*=10
    ender(li)

#Heap Sort
def heapify(li,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and li[i]<li[l]:
        largest=l
    if r<n and li[largest]<li[r]:
        largest=r
    if largest!=i:
        li[i],li[largest]=li[largest],li[i]
        drawer("Heap Sort",li,[i,l,r,largest],n,1)
        heapify(li,n,largest)


def Heap_Sort(li):
    starter(li)
    n=len(li)
    for i in range(n//2 -1,-1,-1):
        heapify(li,n,i)
    for i in range(n-1,0,-1):
        li[i],li[0]=li[0],li[i]
        heapify(li,i,0)
    ender(li)

#Selection Sort
def Selection_Sort(li):
    starter(li)
    for i in range(len(li)):
        min_id=i
        for j in range(i+1,len(li)):
            if li[min_id]>li[j]:
                min_id=j
                drawer("Selection Sort",li,[j,min_id],i-1)
        li[i],li[min_id]=li[min_id],li[i]
        
    ender(li)

#Insertion Sort
def Insertion_Sort(li):
    starter(li)
    for i in range(1,len(li)):
        key=li[i]
        j=i-1
        while j>=0 and key<li[j]:
            li[j+1]=li[j]
            j-=1
            drawer("Insertion Sort",li,[j+1,j],i-1)
        li[j+1]=key
    ender(li)
    return li


#Merge Sort
def merge(li,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(0,n1):
        L[i]=li[l+i]
    for j in range(0,n2):
        R[j]=li[m+1+j]
        
    
    i=0
    j=0
    k=l

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            li[k]=L[i]
            i+=1
            drawer("Merge Sort",li,[i,j],k)
        else:
            li[k]=R[j]
            j+=1
            drawer("Merge Sort",li,[i,j],k)
        k+=1
    
    while i<n1:
        li[k]=L[i]
        i+=1
        k+=1
        drawer("Merge Sort",li,[i,j],k)
    
    while j<n2:
        li[k]=R[j]
        j+=1
        k+=1
        drawer("Merge Sort",li,[i,j],k)

def mergesort(li,l,r):
    if l < r:
        m=(l+(r-1))//2
        drawer("Merge Sort",li,[l,r],m)
        mergesort(li,l,m)
        mergesort(li,m+1,r)
        merge(li,l,m,r)

def Merge_Sort(li):
    starter(li)
    mergesort(li,0,len(li)-1)
    ender(li)

#BubbleSort
def Bubble_Sort(li):
    
    starter(li)
    n=len(li)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                drawer("Bubble Sort",li,[j,j+1],k=n-i-1,rev=1)
    ender(li)


#QuickSort
def exequick(li,start,end):
    if start>=end:
        return
    p=partition(li,start,end)
    exequick(li,start,p-1)
    exequick(li,p+1,end)

def partition(li,start,end):
    pivot=li[start]
    low=start+1
    high=end
    drawer("Quick Sort",li,[low,high],start)
    while True:
        while low<=high and li[high]>=pivot:
            high=high-1
            drawer("Quick Sort",li,[low,high],start)
        while low<=high and li[low]<=pivot:
            low=low+1
            drawer("Quick Sort",li,[low,high],start)
        if low<=high:
            li[low],li[high]=li[high],li[low]
            drawer("Quick Sort",li,[low,high],start)
        else:
            break
    li[start],li[high]=li[high],li[start]
    drawer("Quick Sort",li,[low,high],start)
    return high

def Quick_Sort(li):
    starter(li)
    exequick(li,0,len(li)-1)
    ender(li)
    
def main_menu():
    global screen,allow,sorts,buttonDimensions
    allow=True
    screen.fill((255,255,255))
    myfont=pygame.font.SysFont("kokila",36)
    buttonDimensions=[]
    for i in range(len(sorts)):
        x=((i%2)*255)+10
        y=(((i//2))*90)+10
        width=225
        height=80
        pygame.draw.rect(screen,(100,100,100),(x+2,y+3,width,height))
        pygame.draw.rect(screen,(0,0,0),(x,y,width,height))
        label=myfont.render(sorts[i],1,(255,255,255))
        label_rect=label.get_rect()
        label_rect.center=((x+(width//2),y+(height//2)))
        screen.blit(label,label_rect)
        buttonDimensions.append([x,y,x+width,y+height])
    pygame.display.update()
    eventhandling()
    pygame.quit()
buttonDimensions=[]
sorts=["Quick Sort","Bubble Sort","Merge Sort","Insertion Sort","Selection Sort","Heap Sort","PanCake Sort","Radix Sort","Shell Sort","Bogo Sort","Tim Sort","Comb Sort"]
allow=True
pygame.display.update()
main_menu()