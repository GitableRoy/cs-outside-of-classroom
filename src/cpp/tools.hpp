#ifndef TOOLS_HPP
#define TOOLS_HPP

#include <iostream>
#include <vector>
#include <random>


namespace tools
{

// Convenient typenames
using ull = unsigned long long;
using sll = long long;


// Initialize the random device to obtain a seed for random number generator
std::random_device rd;


// Initialize the random number generation engine using rd as the seed
std::default_random_engine rng(rd());


// Generates a vector filled with random integers
std::vector<sll> rand_int(ull size, sll min = 0, sll max = 100)
{
    // Create a uniform integer distributor with the range [min, max]
    std::uniform_int_distribution<sll> uni_dist(min, max);

    // Fill up a vector with values from that distributor and return it
    std::vector<sll> vec(size);
    for ( auto& elem : vec )
        elem = uni_dist(rng);

    return vec;
}


// Sort a vector of integers using selection sort
void selection_sort(std::vector<sll>& vec)
{
    int size = vec.size();
    int last = vec.size() - 1;
    for ( int i = 0; i < last; ++i )
    {
        int minIdx = i;
        for ( int j = i+1; j < size; ++j )
            if ( vec[minIdx] > vec[j] )
                minIdx = j;

        int temp = vec[minIdx];
        vec[minIdx] = vec[i];
        vec[i] = temp;
    }
}


// Propagate up the heap
void propagate_up(std::vector<sll>& heap)
{
    // Start with the node that was just inserted
    sll current = heap[0];
    while ( current > 1 )
    {
        // Compare with the parent
        // If the parent is smaller, swap
        if ( heap[current] > heap[current/2] )
        {
            // Swap
            int temp = heap[current];
            heap[current] = heap[current/2];
            heap[current/2] = temp;
            
            // Change the index of current to its parent
            current = current/2;
        }
        else
        {
            break;
        }
    }
}


// Heapify a vector
std::vector<sll> heapify(const std::vector<sll>& vec)
{
    ull size = vec.size();
    std::vector<sll> heap(size + 1);
    heap[0] = 1;

    for ( ull i = 0; i < size; i++ )
    {
        // Put the item at the end of the heap
        heap[heap[0]] = vec[i];

        // Propagate that item up the heap
        propagate_up(heap);
        ++heap[0];
    }

    return heap;
}


// Generates a vector filled with random real numbers
std::vector<double> rand_real(ull size, double min = 0.0, double max = 1.0)
{
    // Create a uniform real-value distributor with the range [min, max)
    std::uniform_real_distribution<double> uni_dist(min, max);

    // Fill up a vector with values from that distributor and return it
    std::vector<double> vec(size);
    for ( auto& elem : vec )
        elem = uni_dist(rng);

    return vec;
}


// Checks if the array is sorted
template <typename T>
bool is_sorted(const std::vector<T>& vec)
{
    ull n = vec.size();
    for ( ull i = 1; i < n; ++i )
        if ( vec[i-1] > vec[i] )
            return false;

    return true;
}


}


// Lists the elements of a vector in this style:
// {1, 14, 22, -1, 31}
template <typename T>
std::ostream& operator<<(std::ostream& out, const std::vector<T>& vec)
{
    auto itr = vec.cbegin();
    out << "{" << *itr;
    while ( ++itr != vec.cend() )
        out << ", " << *itr;

    return out << "}";
}


#endif // TOOLS_HPP
