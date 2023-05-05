/*
* decode base64 + fb deserialization time: 0.06..0.08 ms (using -O3 optimization)
* only decode base64 + fb deserialization: 0.006..0.008 ms,
*   i.e. the creation of the json return string adds a lot to the decoding time
* refs:
* https://github.com/gaspardpetit/base64
* https://stackoverflow.com/questions/342409/how-do-i-base64-encode-decode-in-c/41094722#41094722
* https://stackoverflow.com/questions/180947/base64-decode-snippet-in-c
* https://www.boost.org/doc/libs/1_82_0/doc/html/property_tree.html
*/
#include <iostream>
#include <chrono>
#include <string>

#include "decode_classification.hpp"

using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;

void testme() {
	/* Expected output
     * deserialized: {"1":{"C":"593","P":"0.121094"},"2":{"C":"627","P":"0.121094"},"3":{"C":"921","P":"0.121094"},"4":{"C":"95","P":"0.0742188"},"5":{"C":"651","P":"0.0585938"}}
    */
	const std::string encoded = "DAAAAAAABgAKAAQABgAAAAwAAAAAAAYACAAEAAYAAAAEAAAABQAAAEwAAAA0AAAAJAAAABQAAAAEAAAA0P///4sCAAAAAHA93P///18AAAAAAJg96P///5kDAAAAAPg99P///3MCAAAAAPg9CAAMAAQACAAIAAAAUQIAAAAA+D0=";
	auto tic = high_resolution_clock::now();
	std::string deserialized = deserialize(encoded);
	auto toc = high_resolution_clock::now();
	duration<double, std::milli> ms_double = toc - tic;
	std::cout << "decode base64 + fb deserialization time: " << ms_double.count() << " ms" << std::endl;
	std::cout << "deserialized: " << deserialized << std::endl;
}

int main(int /*argc*/, const char * /*argv*/[]) {
	testme();
}