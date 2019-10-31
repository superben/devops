package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequestMapping("/demo")
@ResponseBody
public class DemoViewController {
	@RequestMapping("/index")
	public String index() {
		return "index1234567";
	}
}
