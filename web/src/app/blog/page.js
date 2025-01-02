'use client';

import React from 'react';
import { ArrowLeft } from 'lucide-react';
import { BlogCard } from '../../components/BlogCard';
import { blogPosts } from '../../lib/blog-data';

export default function BlogPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-pink-700 text-white">
      <nav className="container mx-auto px-4 py-6">
        <a 
          href="/"
          className="inline-flex items-center gap-2 text-white hover:text-pink-300"
        >
          <ArrowLeft size={20} />
          Back to Home
        </a>
      </nav>

      <div className="container mx-auto px-4 py-12">
        <header className="text-center mb-12">
          <h1 className="text-4xl font-bold mb-4">MacFaceSwap Blog</h1>
          <p className="text-xl text-pink-100 max-w-2xl mx-auto">
            Tutorials, tips, and updates to help you make the most of MacFaceSwap
          </p>
        </header>

        <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {Object.entries(blogPosts).map(([slug, post]) => (
            <BlogCard key={post.id} post={{ ...post, slug }} />
          ))}
        </div>
      </div>
    </div>
  );
}