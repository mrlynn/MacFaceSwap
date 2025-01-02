'use client';

import React from 'react';
import { Github, Download, ChevronDown, Clock, ChevronRight } from 'lucide-react';
import { BlogCard } from '../components/BlogCard';
import { blogPosts } from '../lib/blog-data';

const LandingPage = () => {
  return (
    <main className="min-h-screen bg-gradient-to-br from-purple-900 to-pink-700 text-white px-4 py-8">
      {/* Hero Section */}
      <div className="container mx-auto px-4 py-16">
        <nav className="flex justify-between items-center mb-16">
          <div className="text-white text-2xl font-bold">MacFaceSwap</div>
          <div className="flex gap-4">
            <a href="#download" className="text-white hover:text-pink-300">Download</a>
            <a href="#about" className="text-white hover:text-pink-300">About</a>
            <a href="#blog" className="text-white hover:text-pink-300">Blog</a>
          </div>
        </nav>

        <div className="flex flex-col items-center text-center mb-16">
          <div className="rounded-3xl bg-gradient-to-br from-purple-600 to-pink-500 p-1 mb-8">
            <img
              src="/icon.png"
              alt="FaceSwap Icon"
              className="w-32 h-32 rounded-3xl"
            />
          </div>
          <h1 className="text-5xl font-bold text-white mb-6">
            Swap Faces With Your Favorite Celebrities
          </h1>
          <p className="text-xl text-pink-100 max-w-2xl mb-8">
            Experience real-time face swapping powered by advanced AI. Create, experiment, and share with our intuitive macOS application.
          </p>

          <div className="relative w-full max-w-4xl mx-auto mb-12 rounded-xl overflow-hidden shadow-2xl">
            <video
              autoPlay
              loop
              muted
              playsInline
              className="w-full rounded-xl"
            >
              <source src="/demo.mp4" type="video/mp4" />
            </video>
          </div>

          <div className="flex gap-4">
            <a
              href="https://github.com/mrlynn/MacFaceSwap/releases/download/v1.0.0/MacFaceSwap_20250101.dmg"
              className="bg-pink-500 hover:bg-pink-600 text-white px-8 py-3 rounded-lg flex items-center gap-2"
            >
              <Download size={20} />
              Download for macOS
            </a>
            <a
              href="https://github.com/mrlynn/MacFaceSwap"
              className="bg-white/10 hover:bg-white/20 text-white px-8 py-3 rounded-lg flex items-center gap-2"
            >
              <Github size={20} />
              View Source
            </a>
          </div>
        </div>

        <div className="flex justify-center">
          <ChevronDown size={32} className="text-white animate-bounce" />
        </div>
      </div>

      {/* Features Section */}
      <div className="bg-black/30 py-24" id="about">
        <div className="container mx-auto px-4">
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-white/5 p-6 rounded-xl">
              <h3 className="text-xl font-bold text-white mb-4">
                Real-Time Processing
              </h3>
              <p className="text-pink-100">
                Experience instant face swapping with our optimized deep learning engine.
              </p>
            </div>
            <div className="bg-white/5 p-6 rounded-xl">
              <h3 className="text-xl font-bold text-white mb-4">
                User Privacy
              </h3>
              <p className="text-pink-100">
                All processing happens locally on your device. Your photos stay private.
              </p>
            </div>
            <div className="bg-white/5 p-6 rounded-xl">
              <h3 className="text-xl font-bold text-white mb-4">
                Native Performance
              </h3>
              <p className="text-pink-100">
                Built specifically for macOS to ensure smooth operation and efficiency.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Download Section */}
      <div className="py-24" id="download">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold text-white mb-8">
            Ready to Transform?
          </h2>
          <div className="flex justify-center gap-8">
            <div className="bg-white/5 p-8 rounded-xl">
              <h3 className="text-xl font-bold text-white mb-4">
                Latest Release
              </h3>
              <p className="text-pink-100 mb-6">
                Version 1.0.0
              </p>
              <a
                href="https://github.com/mrlynn/MacFaceSwap/releases/download/v1.0.0/MacFaceSwap_20250101.dmg"
                className="bg-pink-500 hover:bg-pink-600 text-white px-6 py-3 rounded-lg inline-flex items-center gap-2"
              >
                <Download size={20} />
                Download DMG
              </a>
            </div>
          </div>
        </div>
      </div>
      {/* Blog Section */}
      <div className="py-24 bg-black/30" id="blog">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-white mb-4">
              Learn & Explore
            </h2>
            <p className="text-pink-100 max-w-2xl mx-auto">
              Discover tutorials, tips, and updates to make the most of MacFaceSwap
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {Object.entries(blogPosts).map(([slug, post]) => (
              <BlogCard key={post.id} post={{ ...post, slug }} />
            ))}
          </div>
        </div>
      </div>
    </main>
  );
};

export default LandingPage;