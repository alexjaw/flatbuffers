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

#include "polfosol.h"
#include "classification_generated.h"

#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>

using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;

using namespace dnn_vision;
namespace pt = boost::property_tree;

template < typename Type > std::string to_str (const Type & t)
{
	std::ostringstream os;
	os << t;
	return os.str ();
}

std::string encode(const std::string &bytes) {
	return polfosol::b64encode((unsigned char*)bytes.data(), bytes.length());
}

std::string decode(const std::string &base64) {
	return polfosol::b64decode((unsigned char*)base64.data(), base64.length());
}

std::string deserialize(const std::string &base64) {
	std::string r = "TBD";
	pt::ptree tree;
	std::string s = "";
	//auto tic = high_resolution_clock::now();
	std::string decoded = decode(base64);
	//std::cout << decoded<< std::endl;
	auto detections = GetClassificationTop((unsigned char*)decoded.data());
	auto perception = detections->perception();
	//auto toc = high_resolution_clock::now();
	//duration<double, std::milli> ms_double = toc - tic;
	//std::cout << "decode base64 + fb deserialization time: " << ms_double.count() << " ms" << std::endl;
	auto n = perception->classification_list()->size();
	//std::cout << "n: " << n << std::endl;
	for (unsigned i=0; i<n; ++i) {
		auto class_id = perception->classification_list()->Get(i)->class_id();
		auto score = perception->classification_list()->Get(i)->score();
		//std::cout << "i: " << i << ". class_id:" << class_id << ", score:" << score << std::endl;
		//tmp = boost::json::serialize(boost::json::object{{'C', class_id}, {'P', score}});
		s = to_str(i+1) + ".C";
        tree.put(s, to_str(class_id));
        s = to_str(i+1) + ".P";
        tree.put(s, to_str(score));
	}

	std::stringstream ss;
    pt::json_parser::write_json(ss, tree, false);

	return ss.str();
}