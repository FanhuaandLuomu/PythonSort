# coding:utf-8
# 常见的排序算法 Python实现
# 1.快速排序
# 2.插入排序 2.x 单链表的插入排序
# 3.堆排序
# 4.冒泡排序
# 5.选择排序
# 6.归并排序
# 7.希尔排序

# 1.快速排序
def quickSort(nums):
	quick_sort(nums,0,len(nums)-1)

def quick_sort(array, left, right):
	if left<right:

		index=partion(array,left,right)
		# 递归
		quick_sort(array,left,index)
		quick_sort(array,index+1,right)

def partion(array,left,right):
	key=array[left]
	while left<right:
		while left<right and array[right]>=key:
			right-=1

		if left<right:
			array[left]=array[right]
			

		while left<right and array[left]<key:
			left+=1

		if left<right:
			array[right]=array[left]
			
	array[left]=key
	return left

nums=[2,1,3,5,4,0]
quickSort(nums)
print 'quick_sort:',nums

#===================

# 2.插入排序
def insort(array):

	for j in range(1,len(array)):
		tmp=array[j]

		i=j-1
		while i>=0 and tmp<array[i]:
			# i后移1位
			array[i+1]=array[i]
			i-=1

		array[i+1]=tmp

	return array

nums=[2,1,3,5,4,0]
insort(nums)
print 'insort:',nums

#===========================
# 2.x 链表插入排序
class ListNode:
	def __init__(self,val,next=None):
		self.val=val
		self.next=next

def insertionSortList(head):

	# a. 不设置头结点
	# p=head

	# while p and p.next:
	# 	if p.val<=p.next.val:
	# 		p=p.next
	# 	else:
	# 		# q 待插入节点
	# 		q=p.next
	# 		p.next=q.next
			
	# 		r=head
	# 		# q<r q 是新的head节点
	# 		if r.val>q.val:
	# 			q.next=r
	# 			head=q
	# 		else:
	# 			while r.next and r.next.val<=q.val:
	# 				r=r.next

	# 			q.next=r.next
	# 			r.next=q
	# return head

	# b. 设置新的头结点
	root=ListNode(0)
	root.next=head
	p=head
	while p and p.next:
		if p.val<=p.next.val:
			p=p.next
		else:
			q=p.next
			p.next=q.next
			r=root
			while r.next.val<=q.val:
				r=r.next
			q.next=r.next
			r.next=q
	return root.next


# 可视化链表
def printList(head):
	ilist=[]
	while head:
		ilist.append(head.val)
		head=head.next
	print 'insertionSortList:',ilist 

head=ListNode(2,ListNode(1,ListNode(3,ListNode(5,ListNode(4,ListNode(0))))))

# head=ListNode(1,ListNode(1))

# printList(head)

head=insertionSortList(head)

printList(head)

#===========================

# 3. 堆排序
def heapsort(array):
	i=len(array)/2-1
	while i>=0:
		percDown(array,i,len(array))
		i-=1

	length=len(array)
	index=length-1
	for i in range(length):
		# print i
		array[0],array[index]=array[index],array[0]

		percDown(array,0,index)
		index-=1


def left_child(i):
	return 2*i+1

def percDown(array,i,n):

	tmp=array[i]

	while left_child(i)<n:

		child=left_child(i)
		if child!=n-1 and array[child]<array[child+1]:
			child+=1
		if tmp<array[child]:
			array[i]=array[child]
		else:
			break

		i=child

	array[i]=tmp

nums=[2,1,3,5,4,0]
heapsort(nums)
print 'heapsort:',nums

#=========================
# 4. 冒泡排序

def busort(nums):
	flag=1
	i,j=0,0

	for i in range(len(nums)):
		if flag:
			flag=0
			for j in range(len(nums)-1,i,-1):
				# j:len(nums)-1~~i 小的前移  最终移至i的位置
				if nums[j]<nums[j-1]:
					nums[j],nums[j-1]=nums[j-1],nums[j]
					flag=1
		else:
			break

	return nums

nums=[2,1,3,5,4,0]
print 'busort:',busort(nums)


#=================================
# 5. 选择排序
def selsort(nums):
	# 前一部分已排序 后部分未排序
	# 从未排序区找一个最小值 放入已排序区
	for i in range(len(nums)):
		# i 设为当前最小值 index
		m=i
		for j in range(i+1,len(nums)):
			if nums[j]<nums[m]:
				m=j
		if m!=i:
			nums[m],nums[i]=nums[i],nums[m]
	return nums

nums=[2,1,3,5,4,0]
print 'selsort:',selsort(nums)

#=================================
# 6. 二路归并排序

def merge(nums1,nums2):
	res=[]
	i,j=0,0
	while i<len(nums1) and j<len(nums2):
		if nums1[i]<nums2[j]:
			
			res.append(nums1[i])
			i+=1

		else:
			res.append(nums2[j])
			j+=1

	while i<len(nums1):
		res.append(nums1[i])
		i+=1

	while j<len(nums2):
		res.append(nums2[j])
		j+=1

	return res


def mergeSort(nums):
	if len(nums)>1:
		mid=len(nums)/2
		tmp1=mergeSort(nums[:mid])
		tmp2=mergeSort(nums[mid:])
		res=merge(tmp1,tmp2)
		return res
	# nums为空或只有一个元素时 直接返回nums
	else:
		return nums

nums=[2,1,3,5,4,0]
print 'mergeSort:',mergeSort(nums)

#=================================
# 7. 希尔排序

def shellSort(nums):
	gap=len(nums)/2
	while gap>0:
		# gap组  每组 len(nums)/gap个元素
		for k in range(gap):
			# 组内插入排序

			for i in range(k+gap,len(nums),gap):
				# i 为当前待插入元素
				# j 指向i所在组的前部分元素
				tmp=nums[i]
				j=i-gap

				while j>=k and nums[j]>tmp:
					nums[j+gap]=nums[j]
					j-=gap

				# tmp 插入j的下一个位置
				nums[j+gap]=tmp

		# gap 缩小一半
		gap/=2


nums=[2,1,3,5,4,0]
shellSort(nums)
print 'shellSort:',nums


